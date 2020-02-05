# pylint: disable-msg=R0801
'''
Here we are validating einvoice payload
'''
import time
# import traceback
from io import StringIO
import datetime
import csv
import copy
# import asyncio
import logging
import json
import requests
import boto3
from jsonschema import Draft7Validator
# import pandas as pd
import orjson
from module.util.mis_function import get_error, validate_int
from module.util.dao import SQSService, get_udid, fill_nic_response_data
from module.ewb.configuration import EWB_CSV_HEADER
from module.business.business_validation import schema_business_validate
from module.ewb.ewb_parse import EwbParse
from module.db_interface.irn_master import IrnMaster
from module.db_interface.query_configuration import IRN_MASTER_QUERY, IRN_DTLS_QUERY,\
                                                IRN_MIS_DTLS_QUERY
from settings.configuration import RESPONSE_STRUCTURE, STATUS_CODE, RESPONSE_MESSAGE, FLAG,\
                                STATUS, SAVE_REQUIRED, TRANS_DTLS_CAT_LIST, DOC_DTLS_TYPE_LIST,\
                                PROCESS_NAME, SQS_TEMPLATE, EXTRA_FIELD_APPEND
from settings.redis_cache import RedisCache
from settings.db_config import irn_insert_query_execute
from .schema_configuration import HSN_SCHEMA
LOGGER = logging.getLogger("einvoice_app")

def header_validate(req):
    '''
    Here we are validating headers
    params - headers - headers dict from request
    '''
    start_time = time.time()
    LOGGER.info("Start header_validate")
    response_body = copy.deepcopy(RESPONSE_STRUCTURE)
    header_check = ["token", "customer_id"]
    response_list = []
    for header in header_check:
        LOGGER.info(req.get_header(header))
        if not req.get_header(header):
            error_dict = get_error(f"{header} is missing", header, "Error")
            response_body["pwc_response"]["validation_remarks"].append(error_dict)
    if not validate_int(req.get_header("customer_id", default="")):
        error_dict = get_error("customer_id must be integer", "customer_id", "Error")
        response_body["pwc_response"]["validation_remarks"].append(error_dict)
    if req.get_header("invoice_count") and not validate_int(req.get_header("invoice_count")):
        error_dict = get_error("invoice_count must be integer", "invoice_count", "Error")
        response_body["pwc_response"]["validation_remarks"].append(error_dict)
    if response_body["pwc_response"]["validation_remarks"]:
        response_body["pwc_response"]["status"] = STATUS_CODE["AUTH_FAILED"]
        response_body["pwc_response"]["message"] = RESPONSE_MESSAGE["AUTH_FAILED"]
        response_body["pwc_response"]["validation_status"] = STATUS["ERROR"]
        response_list.append(response_body)

    LOGGER.info("End header_validate , time taken %s", format((\
        time.time() - start_time) * 1000, '.2f'))
    return response_list

def customer_validate(req, env):
    '''
    Here we are validating customer_id and token and return client configuration
    params - req: request header
    params - env: environment variable
    '''
    start_time = time.time()
    LOGGER.info("Start customer_validate")
    flag, message = False, ""
    LOGGER.info("token is -> %s", req.get_header("token"))
    customer_id = req.get_header("customer_id")
    LOGGER.info("customer_id is -> %s", customer_id)
    client_config = RedisCache.get_client_config(customer_id, env)
    # LOGGER.info(client_config)
    if not client_config:
        message = "client_configuration file is missing/invalid"
    elif req.get_header("token") != client_config.get("database").get("token", ""):
        message = "token is invalid/missing"
    else:
        flag = True
        # client_config = client_config[customer_id]
    LOGGER.info("End customer_validate, time taken %s", format(\
        (time.time() - start_time) * 1000, '.2f'))
    return flag, message, client_config

def push_to_irp(res_body, customer_id, req_body, email_ids, token):
    # pylint: disable-msg=W0703
    '''
        Call irp API
        params - res_body: response body structure
        params - customer_id: client id
        params - req_body: request body
        params - email_ids: email ids seprated with comma
        token - client token
    '''
    try:
        gstin = req_body.get('User_GSTIN')
        if not gstin:
            gstin = req_body.get('SellerDtls', {}).get('Gstin', '')
        headers_data = {"Content-Type": "application/json",\
            "gstin": gstin,\
            "customerId": customer_id,\
            "token": token}
        url = "http://11.0.1.130:1010/v1/eInvoiceApi"
        resp = requests.post(url, headers=headers_data, data=orjson.dumps(req_body),\
            timeout=60)
        # if resp.status_code == 200:
        res_body["irp_response"] = json.loads(resp.content)

        is_generate = False
        if "error" in res_body["irp_response"]:
            if res_body["irp_response"]["error"]:
                res_body["pwc_response"]["message"] += f", {RESPONSE_MESSAGE['IRP_GEN_FAILED']}"
            else:
                res_body["pwc_response"]["message"] += \
                    f", {RESPONSE_MESSAGE['IPR_GEN_PASSED']}"
                is_generate = True
            fill_nic_response_data(req_body, res_body["irp_response"])
        else:
            res_body["pwc_response"]["message"] += f", {RESPONSE_MESSAGE['IRP_GEN_FAILED']}"
        sqs_temp = SQS_TEMPLATE['IPR_GEN_PASSED'] if is_generate else \
            SQS_TEMPLATE['IRP_GEN_FAILED']
        SQSService.exception_sending(customer_id, PROCESS_NAME["IRN_GENERATE"], sqs_temp,\
            email_ids, response_body=[res_body])
        LOGGER.info(f"CustomerID {customer_id}: PRCOESSALL: IRP API Response {resp.content}")
    except Exception as error:
        LOGGER.error(f"CustomerID {customer_id}: PRCOESSALL: EXCEPTION: "\
            f"IRP API CALL -> {error}", exc_info=True)
        res_body["pwc_response"]["message"] += f", {RESPONSE_MESSAGE['IRP_GEN_FAILED']}"
        SQSService.exception_sending(customer_id, PROCESS_NAME["IRN_GENERATE"],\
            SQS_TEMPLATE['IRP_GEN_FAILED'], email_ids, response_body=[res_body],\
            error_message=str(error))

# this function is invoked from payload_validate function
def payload_validate(payload, load_id, client_configuration, ewb_list, customer_id, email_ids,\
    irn_mstr_list, irn_dtls_list, irn_mis_dtls_list):
    # pylint: disable-msg=R0801
    '''
    validating einvoice payload
    params - payload: payload is request body
    params - load_id: load_id of upload table
    params - client_configuration: configuration of client
    params - ewb_list: appending ewb data
    params - customer_id: client id
    params - email_ids: email ids seprated with comma
    params - irn_mstr_list: inserting data into irn_master if flag save = Y
    params - irn_dtls_list:inserting data into irn_master if flag save = Y
    params - irn_mis_dtls_list: params - irn_mis_dtls_list appending the
        data to irn_mis_dtls_list
    '''
    # appending extra field in response body
    default_value = copy.deepcopy(EXTRA_FIELD_APPEND)
    default_value['load_id'] = payload["load_id"] = load_id
    res_body = schema_business_validate(payload, client_configuration, email_ids, customer_id)
    res_body["pwc_response"].update(default_value)
    res_body["irp_response"] = {}
    if res_body['pwc_response']['status'] in SAVE_REQUIRED:
        payload['udid'] = get_udid(payload)
        res_body["pwc_response"]['udid'] = payload['udid']
    if res_body["pwc_response"]["status"] == STATUS_CODE["SUCCESS"]:
        # is_irn validation
        if not payload.get("is_irn"):
            trans_flag = payload["TranDtls"]["Catg"] in TRANS_DTLS_CAT_LIST
            doc_flag = payload["DocDtls"]["Typ"] in DOC_DTLS_TYPE_LIST
            res_body["pwc_response"]["is_irn"] = FLAG["YES"] if \
                (trans_flag and doc_flag) else FLAG["NO"]
            res_body["pwc_response"]["message"] += f", {RESPONSE_MESSAGE['IRN_DETERMINE']}"
            payload["is_irn"] = res_body["pwc_response"]["is_irn"]
        else:
            res_body["pwc_response"]["is_irn"] = payload["is_irn"]
        if res_body["pwc_response"]["is_irn"] == FLAG["NO"] and client_configuration.get(\
            'auto_exclude', "") == FLAG["YES"]:
            res_body["pwc_response"]["is_exclude"] = FLAG["YES"]
            payload["is_exclude"] = FLAG["YES"]
            payload["exclude_reason"] = RESPONSE_MESSAGE["IRN_EXC_RSN"]
        # checking auto_data_push_to_irp is required or not
        if res_body["pwc_response"]["is_irn"] == FLAG["YES"]:
            if client_configuration.get("push_to_irp", "") == FLAG["YES"]:
                push_to_irp(res_body, customer_id, payload, email_ids,\
                    client_configuration["database"]["token"])
            else:
                res_body["pwc_response"]["message"] += f", {RESPONSE_MESSAGE['IRP_FLAG_FALSE']}"
        else:
            res_body["pwc_response"]["message"] += f", {RESPONSE_MESSAGE['IS_IRN_NOT_REQUIRD']}"

    if client_configuration.get("push_to_db", "") == FLAG["YES"]:
        if res_body['pwc_response']['status'] in SAVE_REQUIRED and client_configuration.get(\
            "validation", "") == FLAG["YES"]:
            IrnMaster.get_irn_master(payload, irn_mstr_list, irn_dtls_list, irn_mis_dtls_list,\
                res_body)
        else:
            IrnMaster.failure_data_irn_master(payload, irn_mstr_list, irn_dtls_list,\
                irn_mis_dtls_list, res_body)
    # is_ewb validation
    if client_configuration.get('push_to_ewb', "") == FLAG["YES"]:
        if not payload.get("is_ewb"):
            hsn_validator = Draft7Validator(HSN_SCHEMA)
            hsn_errors = sorted(hsn_validator.iter_errors(payload), key=lambda e: e.path)
            res_body["pwc_response"]["is_ewb"] = FLAG["YES"]
            if hsn_errors and len(hsn_errors) == len(payload['ItemList']):
                res_body["pwc_response"]["is_ewb"] = FLAG["NO"]
            payload["is_ewb"] = res_body["pwc_response"]["is_ewb"]
        else:
            res_body["pwc_response"]["is_ewb"] = payload["is_ewb"]
        # creating ewb data from payload and appending to ewb_list
        EwbParse.ewb_json_csv_parse(payload, ewb_list)
    return res_body

def upload_csv(ewb_list, bucket_name, customer_id, req_body, email_ids):
    # pylint: disable-msg=W0703
    '''
        Here we are creating csv and uploading to client bucket
        params - ewb_list: dict of list
        params - bucket_name: bucket name of client
        params - customer_id: client id
        params - req_body: request body
        params - email_ids: email ids seprated with comma
    '''
    try:
        LOGGER.info(f"CustomerID {customer_id}: PRCOESSALL: Start creating csv and "\
            f"uploading process")
        writefile = StringIO()
        wrcsv = csv.DictWriter(writefile, delimiter=',', fieldnames=EWB_CSV_HEADER, \
                lineterminator='\n')
        wrcsv.writeheader()
        wrcsv.writerows(ewb_list)
        s3_object = boto3.resource('s3')
        time_stamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        file_name = "incoming-file/Document_Details@SAP@" + time_stamp + ".csv"
        s3_object.Object(bucket_name, file_name).put(Body=writefile.getvalue())
        LOGGER.info(f"CustomerID {customer_id}: PRCOESSALL: CSV file successfully "\
            f"uploaded in client bucket")
    except Exception as error:
        LOGGER.error(f"CustomerID {customer_id}: PRCOESSALL: EXCEPTION: "\
            f"CSV UPLOADING Exception -> {error}", exc_info=True)
        SQSService.exception_sending(customer_id, PROCESS_NAME["IRN_GENERATE"],\
            SQS_TEMPLATE['EXCEPTION'], email_ids, error_message=str(error))

def schema_validate(req_body, load_id, client_configuration, customer_id, email_ids):
    # pylint: disable-msg=R0801
    '''
    here we are doing json schema validation
    params - req_body: request body
    params - load_id: load id of upload table
    params - client_configuration: configuration of client
    params - customer_id: client id
    params - email_ids: email ids seprated with comma
    '''
    start_time = time.time()
    LOGGER.info(f"CustomerID {customer_id}: PRCOESSALL : Start schema_validate")
    response_list = []
    # ewb data list
    ewb_list = []
    # irn master table list
    irn_mstr_list, irn_dtls_list, irn_mis_dtls_list = [], [], []
    for data in req_body:
        response_list.append(payload_validate(data, load_id, client_configuration, ewb_list,\
            customer_id, email_ids, irn_mstr_list, irn_dtls_list, irn_mis_dtls_list))
    # uploading csv file to client bucket
    if ewb_list and client_configuration.get("bucket_name"):
        upload_csv(ewb_list, client_configuration.get("bucket_name"), customer_id, req_body,\
            email_ids)

    if irn_mstr_list:
        irn_insert_query_execute(IRN_MASTER_QUERY, irn_mstr_list,\
            IRN_DTLS_QUERY, irn_dtls_list, IRN_MIS_DTLS_QUERY, irn_mis_dtls_list,\
            client_configuration["database"], customer_id, email_ids)

    LOGGER.info(f"CustomerID {customer_id}: PRCOESSALL : End schema_validate, "\
        f"time taken {format((time.time() - start_time) * 1000, '.2f')}")
    return response_list
