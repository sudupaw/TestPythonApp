'''
Here we are creating einvoice-app-falcon
'''
import os
import time
import copy
import logging
from logging.handlers import TimedRotatingFileHandler
import json
import orjson
import falcon
from module.schema_validation.request_validation import header_validate, customer_validate,\
    schema_validate
from module.business.business_validation import business_rules_validate
from module.util.mis_function import get_error, validate_req_body_structure
from module.util.dao import SQSService
from module.db_interface.upload_details import Upload
from settings.configuration import RESPONSE_STRUCTURE, STATUS_CODE, RESPONSE_MESSAGE, STATUS,\
    PROCESS_NAME, SQS_TEMPLATE
from settings.db_config import create_connection, get_dict_cursor, exist_conn_closed,\
    exist_cur_conn_closed
LOGGER = logging.getLogger('einvoice_app')
LOGGER.setLevel(logging.INFO)
LOGFILENAME = "einvoice-app-log.log"
FORMATTER = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOGHANDLER = TimedRotatingFileHandler('/root/einvoice-falcon-dev/' + LOGFILENAME,\
    when='midnight', interval=1, backupCount=7)
LOGHANDLER.setLevel(logging.INFO)
LOGHANDLER.setFormatter(FORMATTER)
LOGHANDLER.suffix = "%Y%m%d"
LOGGER.addHandler(LOGHANDLER)

ERROR_CODE = {500: falcon.HTTP_500,\
    401: falcon.HTTP_401,\
    400: falcon.HTTP_400,\
    200: falcon.HTTP_200,\
}
# Get ENV VARIABLE
ENV = os.environ.get("env", "qa")

class Einvoice:
    '''
    Here we are calling einvoice api
    purpose - This class does following action
        1. validating header
        2. validating customer_id
        3. validating json schema
        4. call schema_business_validate func fot business rules and schema validation
        5. datermine and set is_irn, is_ewb
        6. push_to_ewb
        7.push_to_irp
    '''
    # @header_validate
    # @body_validate
    def on_post(self, req, resp):
        # pylint: disable-msg=R0914
        # pylint: disable-msg=R0201
        # pylint: disable-msg=E1101
        # pylint: disable-msg=W0703
        '''
        This is einvoice-payload-validate API

        '''
        customer_id = ""
        req_payload = req.stream.read()
        email_ids = req.get_header("email", default="")
        conn = None
        try:
            LOGGER.info("Start Einvoice Process")
            start_time = time.time()
            # getting request body
            response_code, response_list = 200, []
            # header_validate
            response_list = header_validate(req)
            if response_list:
                SQSService.exception_sending(customer_id, PROCESS_NAME["IRN_GENERATE"],\
                    SQS_TEMPLATE["AUTH_FAILED"], email_ids, response_list)
                resp.body = orjson.dumps(response_list)
                resp.status = falcon.HTTP_403
                return
            # validating customer_id and token
            flag, message, client_configuration = customer_validate(req, ENV)
            # checking customer_id and token is valid or not
            if not flag:
                error_dict = get_error(message, "customer_id/token", "Error")
                response_body = copy.deepcopy(RESPONSE_STRUCTURE)
                response_body["pwc_response"]["message"] = RESPONSE_MESSAGE["AUTH_FAILED"]
                response_body["pwc_response"]["status"] = STATUS_CODE["AUTH_FAILED"]
                response_body["pwc_response"]["validation_remarks"].append(error_dict)
                response_body["pwc_response"]["validation_status"] = STATUS["ERROR"]
                response_list = [response_body]
                SQSService.exception_sending(customer_id, PROCESS_NAME["IRN_GENERATE"],\
                    SQS_TEMPLATE["AUTH_FAILED"], email_ids, response_list)
            else:
                conn = create_connection(client_configuration['database'])
                cursor = get_dict_cursor(conn)
                load_id = Upload.get_load_id(cursor)
                customer_id = req.get_header("customer_id")
                LOGGER.debug(f"CustomerID {customer_id}: PROCESSALL: Request Payload: "\
                    f"{req_payload}")
                req_body = json.loads(req_payload)
                if req.get_header("invoice_count"):
                    invoice_count = int(req.get_header("invoice_count"))
                    response_list = validate_req_body_structure(req_body, invoice_count, load_id)
                if not response_list:
                    # here we are validating einvoice payload
                    response_list = schema_validate(req_body, load_id, client_configuration,\
                        customer_id, email_ids)
                else:
                    SQSService.exception_sending(customer_id, PROCESS_NAME["IRN_GENERATE"],\
                        SQS_TEMPLATE["AUTH_FAILED"], email_ids, response_list)
                Upload.insert_load_id(req, req_payload, response_list, load_id, conn, cursor,\
                    client_configuration['database'])
                exist_cur_conn_closed(conn, cursor)
            LOGGER.info(f"CustomerID {customer_id}: PROCESSALL: End Einvoice Process, "\
                f"time taken -> , {format((time.time() - start_time) * 1000, '.2f')}")
            # returning response
            resp.body = orjson.dumps(response_list)
            resp.status = ERROR_CODE[response_code]
        except Exception as error:
            exist_conn_closed(conn)
            LOGGER.error(f"CustomerID {customer_id}: PROCESSALL: EXCEPTION : {error}",\
                exc_info=True)
            SQSService.exception_sending(customer_id, PROCESS_NAME["IRN_GENERATE"],\
                SQS_TEMPLATE["EXCEPTION"], email_ids, error_message=str(error))
            response_body = copy.deepcopy(RESPONSE_STRUCTURE)
            response_body["pwc_response"]["message"] = ("Internal Server Error, Please contact to "\
                "help desk")
            response_body["pwc_response"]["status"] = STATUS_CODE["EXCEPTION"]
            response_body["pwc_response"]["validation_status"] = "Exception"
            resp.body = orjson.dumps([response_body])
            resp.status = falcon.HTTP_200
        LOGGER.info(f"CustomerID {customer_id}: PROCESSALL: Response Body: {resp.body}")
        return

    # # @header_validate
    def on_get(self, req, resp):
        # pylint: disable-msg=R0201
        # pylint: disable-msg=W0613
        '''
        Resource is not available.
        '''
        quote = {
            'success': True,
            'name': 'py_validation_rules'
        }
        resp.media = quote

# class EinvoiceValidation:
#     """docstring for EinvoiceValidation"""
#     def on_post(self, req, resp):
#         # pylint: disable-msg=R0914
#         # pylint: disable-msg=R0201
#         # pylint: disable-msg=E1101
#         # pylint: disable-msg=W0703
#         '''
#         purpose - This class does following action
#             1. validating header
#             2. validating customer_id
#             3. validating json schema
#             4. validating business rules
#         '''
#         customer_id = ""
#         req_payload = req.stream.read()
#         email_ids = req.get_header("email", default="")
#         try:
#             LOGGER.info("Start Einvoice Process")
#             start_time = time.time()
#             # getting request body
#             response_code, response_list = 200, []
#             # header_validate
#             response_list = header_validate(req)
#             if response_list:
#                 resp.body = orjson.dumps(response_list)
#                 resp.status = falcon.HTTP_403
#                 return
#             # validating customer_id and token
#             flag, message, client_configuration = customer_validate(req)

#             # checking customer_id and token is valid or not
#             if not flag:
#                 error_dict = get_error(message, "customer_id/token", "Error")
#                 response_body = copy.deepcopy(RESPONSE_STRUCTURE)
#                 response_body["pwc_response"]["message"] = "Authentiction failed"
#                 response_body["pwc_response"]["status"] = STATUS_CODE["AUTH_FAILED"]
#                 response_body["pwc_response"]["validation_remarks"].append(error_dict)
#                 response_list = [response_body]
#             else:
#                 customer_id = req.get_header("customer_id")
#                 LOGGER.info(f"CustomerID {customer_id}: SCHEMA_BUSINESS VALIDATION API: "\
#                     f"Request Payload: {req_payload}")
#                 req_body = orjson.loads(req_payload)
#                 # here we are validating invoice count
#                 if req.get_header("invoice_count"):
#                     invoice_count = int(req.get_header("invoice_count"))
#                     response_list = validate_req_body_structure(req_body, invoice_count)
#                 if not response_list:
#                     # here we are validating einvoice payload
#                     response_list = business_rules_validate(req_body, client_configuration,\
#                         customer_id, email_ids)
#             LOGGER.info(f"CustomerID {customer_id}: SCHEMA_BUSINESS VALIDATION API: End Einvoice "\
#                 f"Process, time taken -> , {format((time.time() - start_time) * 1000, '.2f')}")
#             # returning response
#             resp.body = orjson.dumps(response_list)
#             resp.status = ERROR_CODE[response_code]
#         except Exception as error:
#             LOGGER.error(f"CustomerID {customer_id}: SCHEMA_BUSINESS VALIDATION API: "\
#                 f"EXCEPTION : {error}", exc_info=True)
#             SQSService.exception_sending(customer_id, "SCHEMA_BUSINESS VALIDATION API",\
#                 req_payload, str(error), "getting some exception", email_ids)
#             response_body = copy.deepcopy(RESPONSE_STRUCTURE)
#             response_body["pwc_response"]["message"] = ("Internal Server Error, Please contact to "\
#                 "help desk")
#             response_body["pwc_response"]["status"] = STATUS_CODE["EXCEPTION"]
#             response_body["pwc_response"]["validation_status"] = "Exception"
#             resp.body = orjson.dumps([response_body])
#             resp.status = falcon.HTTP_200
#         LOGGER.info(f"CustomerID {customer_id}: SCHEMA_BUSINESS VALIDATION API: "\
#             f"Response Body: {resp.body}")
#         return

APP = falcon.API()

APP.add_route('/v1/einvoice', Einvoice())
# APP.add_route('/v1/einvoice/rulesvalidation', EinvoiceValidation())
