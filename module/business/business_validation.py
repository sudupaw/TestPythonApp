'''
Here we are validating json schema and business logic
'''
# pylint: disable-msg=R0801
import time
import copy
import datetime
import logging
import json
from jsonschema import Draft7Validator
from settings.configuration import RESPONSE_STRUCTURE, STATUS_CODE, RESPONSE_MESSAGE, FLAG,\
    STATUS, PROCESS_NAME, SQS_TEMPLATE
from settings.email_service import send_email
from module.schema_validation.schema_configuration import SCHEMA
from module.util.mis_function import get_error
from module.util.dao import SQSService
from .transformation import TransformData, ValDtlsTransform
LOGGER = logging.getLogger("einvoice_app")


def validate_date(row, rule, res_body, alert_error_status):
    '''
        Here we are validating date
        params - row: payload
        params - rule: business logic rule
        params - res_body: response bodye
        params - alert_error_status: menage error/alert validation status
    '''
    # creating date_obj
    date_obj = datetime.datetime.strptime(row["DocDtls"]["Dt"], "%Y-%m-%d")
    # creating current datetime object
    current_date = datetime.datetime.now()
    if date_obj > current_date:
        error_dict = get_error(rule["validation_remark"], "DocDtls.Dt", rule["validation_status"])
        if rule["validation_status"] not in alert_error_status:
            alert_error_status.append(rule["validation_status"])

        res_body["pwc_response"]["validation_remarks"].append(error_dict)


def validate_bu(row, rule, res_body, alert_error_status):
    '''
        Here we are validating bu
        params - row: payload
        params - rule: business logic rule
        params - res_body: response bodye
        params - alert_error_status: menage error/alert validation status
    '''
    if row.get("bu_flag"):
        error_dict = get_error(rule["validation_remark"], "bu", rule["validation_status"])
        if rule["validation_status"] not in alert_error_status:
            alert_error_status.append(rule["validation_status"])
        res_body["pwc_response"]["validation_remarks"].append(error_dict)

def validate_sbu(row, rule, res_body, alert_error_status):
    '''
        Here we are validating sbu
        params - row: payload
        params - rule: business logic rule
        params - res_body: response bodye
        params - alert_error_status: menage error/alert validation status
    '''
    if row.get("sbu_flag"):
        error_dict = get_error(rule["validation_remark"], "sbu", rule["validation_status"])
        if rule["validation_status"] not in alert_error_status:
            alert_error_status.append(rule["validation_status"])
        res_body["pwc_response"]["validation_remarks"].append(error_dict)

def validationrow(row, client_configuration, res_body):
    '''
        Here we are validating request data
        params - row: request payload
        params - rules: rules of dict
    '''
    alert_error_status = []
    # checking document_date validation is required or not
    for rule in client_configuration["rules"].values():
        if rule["validation_flag"] == FLAG["YES"]:
            func = eval(rule["function_name"])
            func(row, rule, res_body, alert_error_status)

    if alert_error_status:
        res_body["pwc_response"]["validation_status"] = STATUS["ERROR"] if STATUS["ERROR"] in \
            alert_error_status else STATUS["ALERT"]
        res_body["pwc_response"]["message"] += f", {RESPONSE_MESSAGE['BSN_VAL_FAILED']}"
        res_body["pwc_response"]["status"] = STATUS_CODE["BSN_VAL_FAILED"]

# this function is invoked from payload_validate function
def schema_business_validate(payload, client_configuration, email_ids, customer_id):
    # pylint: disable-msg=R0801
    '''
    validating einvoice payload
    params - payload: payload is request body
    params - client_configuration: configuration of client
    params - email_ids: client email_id
    params - customer_id: client id
    '''
    if not "Version" in payload:
        payload["Version"] = "1.00"
    # adding valdtls node if does not exist in payload
    ValDtlsTransform.transform_valdtls(payload)
    validator = Draft7Validator(SCHEMA)
    res_body = copy.deepcopy(RESPONSE_STRUCTURE)
    res_body["pwc_response"]["message"] = RESPONSE_MESSAGE['AUTH_PASSED']
    res_body["pwc_response"]["invoice_number"] = payload.get("DocDtls", {}).get("No", "")
    res_body["pwc_response"]["document_date"] = payload.get("DocDtls", {}).get("Dt", "")
    res_body["pwc_response"]["document_type"] = payload.get("DocDtls", {}).get("Typ", "")
    gstin = payload.get('User_GSTIN')
    if not gstin:
        gstin = payload.get('SellerDtls', {}).get('Gstin', '')
    res_body["pwc_response"]["gstin"] = gstin
    # transformation
    TransformData.transform_mis(payload, client_configuration, res_body, customer_id)
    if client_configuration.get("validation", "") == FLAG["YES"]:
        errors = sorted(validator.iter_errors(payload), key=lambda e: e.path)
        # checking if errors then create error response
        if errors:
            for error in errors:
                error_dict = get_error(error.message, ".".join(\
                    str(x) for x in error.relative_path), "Error")
                res_body["pwc_response"]["validation_remarks"].append(error_dict)
            res_body["pwc_response"]["message"] += f", {RESPONSE_MESSAGE['SCH_VAL_FAILED']}"
            res_body["pwc_response"]["validation_status"] = STATUS["ERROR"]
            res_body["pwc_response"]["status"] = STATUS_CODE["SCH_VAL_FAILED"]
            # sending sqs for schema validation failed
            SQSService.exception_sending(customer_id, PROCESS_NAME["IRN_GENERATE"],\
                SQS_TEMPLATE["SCH_VAL_FAILED"], email_ids, [res_body], payload)
            # is_exclude validation
        else:
            res_body["pwc_response"]["message"] += f", {RESPONSE_MESSAGE['SCH_VAL_PASSED']}"
            res_body["pwc_response"]["validation_status"] = STATUS["SUCCESS"]
            res_body["pwc_response"]["status"] = STATUS_CODE["SUCCESS"]

            validationrow(payload, client_configuration, res_body)
            if res_body["pwc_response"]["status"] == STATUS_CODE["SUCCESS"]:
                res_body["pwc_response"]["message"] += f", {RESPONSE_MESSAGE['BSN_VAL_PASSED']}"
            else:
                # sending sqs for business logic failed
                SQSService.exception_sending(customer_id, PROCESS_NAME["IRN_GENERATE"],\
                    SQS_TEMPLATE["BSN_VAL_FAILED"], email_ids, [res_body], payload)
        if res_body["pwc_response"]["validation_remarks"]:
            if email_ids:
                send_email(email_ids, json.dumps(res_body))
    else:
        res_body["pwc_response"]["status"] = STATUS_CODE["SUCCESS"]
        res_body["pwc_response"]["validation_status"] = STATUS["SUCCESS"]
        res_body["pwc_response"]["message"] = RESPONSE_MESSAGE["VAL_NT_REQ"]
    return res_body

def business_rules_validate(req_body, client_configuration, customer_id, email_ids):
    # pylint: disable-msg=R0801
    '''
    here we are doing json schema validation
    params - req_body: request body
    params - client_configuration: configuration of client
    params - email_ids: client email id
    '''
    start_time = time.time()
    LOGGER.info(f"CustomerID {customer_id}: SCHEMA_BUSINESS VALIDATION API: Start schema_validate")
    response_list = []
    # ewb data list
    for data in req_body:
        response_list.append(schema_business_validate(data, client_configuration, email_ids,\
            customer_id))
    LOGGER.info(f"CustomerID {customer_id}: SCHEMA_BUSINESS VALIDATION API : End schema_validate,"\
        f" time taken {format((time.time() - start_time) * 1000, '.2f')}")
    return response_list
