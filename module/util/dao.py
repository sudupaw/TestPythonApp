'''
Here we are prepare irn_master, irn_details, irn_custom data
'''
import logging
import json
import hashlib
import datetime
import boto3
import fiscalyear
from settings.configuration import FIN_STRT_MNTH, RESPONSE_MESSAGE
LOGGER = logging.getLogger("einvoice_app")

def generate_irn_number(supplier_gstin, invoice_number, invoice_date):
    '''
    Here we are generating irn number
    params - supplier_gstin, supplier_gstin
    params - invoice_number: invoice number
    params - invoice_date: invoice_number
    '''
    irn_number = supplier_gstin + invoice_number + invoice_date
    result = hashlib.sha256(irn_number.encode())
    return result.hexdigest()

class SQSService:
    '''
        All sqs related work are here
    '''
    def __init__(self):
        '''
        object initiate
        '''
        pass

    def __str__(self):
        '''
        object representation
        '''
        LOGGER.info("SQSService object")

    @staticmethod
    def exception_sending(customer_id, api_name, template, email_ids, response_body='',\
        request_payload='', error_message=''):
        '''
            it is static method
            here we are sending exception message to sqs
            params - customer_id: Client ID
            params - api_name: API Name
            params - request_payload: request body
            params - error_message: exception message
            params - email_ids: email ids seprated with comma
            params - response_body: response body
        '''
        sqs_message = {"customer_id": customer_id,\
            "process": api_name,\
            "template": template,\
            "to": email_ids,\
            "request payload": request_payload,\
            "response payload": response_body,\
            "message": error_message,\
        }
        client = boto3.client('sqs', region_name='ap-south-1')
        response = client.send_message(\
            QueueUrl="https://sqs.ap-south-1.amazonaws.com/288123262604/einvoice-app-dev",\
            MessageBody=json.dumps(sqs_message))

def get_udid(payload):
    '''
        Here we are generating udid
        params - payload: request body
    '''
    udid = ""
    try:
        gstin = payload.get('User_GSTIN')
        if not gstin:
            gstin = payload.get('SellerDtls', {}).get('Gstin', '')
        fiscalyear.START_MONTH = FIN_STRT_MNTH
        cur_y = fiscalyear.FiscalYear(datetime.datetime.strptime(\
            payload['DocDtls']['Dt'], '%Y-%m-%d').year)
        fin_y = cur_y.start.date().strftime('%Y') + "-" + cur_y.end.date().strftime('%y')
        if gstin and payload.get('DocDtls', {}).get('Typ') and payload.get('DocDtls', {}).get('No'):
            udid = gstin + fin_y + payload['DocDtls']['Typ'] + \
            payload['DocDtls']['No']
    except Exception as error:
        LOGGER.error(f"exception on udid creating")
    return udid

def fill_nic_response_data(req_body, nic_data):
    '''
        Here we get nic response data
        params - req_body: request body
        params - nic_data: nic payload
    '''
    req_body["irn"] = nic_data.get("data", {}).get(\
        "nic_response_data", {}).get("Irn", "")
    req_body["ackno"] = nic_data.get("data", {}).get(\
        "nic_response_data", {}).get("AckNo", None)
    req_body["ackdt"] = nic_data.get("data", {}).get(\
        "nic_response_data", {}).get("AckDt", None)
    req_body["signedinvoice"] = nic_data.get("data", {}).get(\
        "nic_response_data", {}).get("SignedInvoice", "")
    req_body["signedqrcode"] = nic_data.get("data", {}).get(\
        "nic_response_data", {}).get("SignedQRCode", "")
    req_body["nic_response_encoded"] = json.dumps(nic_data.get(\
        "data", {}).get("nic_response_encoded", ""))
    req_body["nic_gen_mode"] = nic_data.get("data", {}).get("nic_gen_mode", "")
    req_body["nic_response_created_date"] = nic_data.get("data", {}).get(\
        "nic_response_created_date", None)
    req_body["nic_document_status_created_date"] = nic_data.get("data", {}).get(\
        "nic_document_status_created_date", None)

    req_body["nic_response_status"] = nic_data.get("data", {}).get("nic_response_status", "")
    req_body["nic_status"] = nic_data.get("data", {}).get("nic_status", "")

    payload = nic_data.get("data", {}).get("nic_request_payload", "")
    req_body["nic_request_payload"] = json.dumps(payload) if payload else ''

    pln_text = nic_data.get("data", {}).get("nic_response_plaintext_json", "")
    req_body["nic_response_plaintext_json"] = json.dumps(pln_text) if pln_text else ''

    nic_header = nic_data.get("data", {}).get("nic_request_header", "")
    req_body["nic_header"] = json.dumps(nic_header) if nic_header else ''
    err_dtls = nic_data.get('data', {}).get('error_details', '')
    req_body['nic_error_details'] = json.dumps(err_dtls) if err_dtls else ''
    req_body['nic_qr_image'] = json.dumps(nic_data.get("data", {}).get("qr_image", {}))
    req_body['irn_status'] = RESPONSE_MESSAGE['IRN_SUCCESS'] if not nic_data.get('error') else \
        RESPONSE_MESSAGE['IRN_FAILED']
    req_body['report_url'] = nic_data.get('data', {}).get('report_url', '')
    req_body['irp_response_message'] = nic_data.get('message', '')
    req_body['irp_response_error'] = nic_data.get('error')
