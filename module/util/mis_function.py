'''
function
'''
import time
import datetime
import copy
import logging
import redis
import orjson
from settings.configuration import RESPONSE_STRUCTURE, STATUS_CODE, RESPONSE_MESSAGE, STATUS
LOGGER = logging.getLogger("einvoice_app")

def get_error(remark, field_name, validation_status):
    '''
        Here we are creating error dict
        params - remark: validation remark
        params - field_name: error field name
        params - validation_status: validation status Error/Alert
    '''
    return {"remark": remark, "field_name": field_name, "validation_status": validation_status}

def validate_int(data):
    '''
    here we are validating data is int or not
    params - data: string
    '''
    flag = True
    try:
        data = int(data)
        flag = bool(data > 0)
    except ValueError:
        flag = False
    return flag

def parse_date(data):
    # pylint: disable-msg=W0703
    '''
    Here we are converting date format to new date format for table.
    params - data: date string
    '''
    new_data = None
    try:
        new_data = datetime.datetime.strptime(data, '%d-%m-%Y').strftime('%Y-%m-%d')
    except Exception as error:
        LOGGER.warning(str(error))
    return new_data

def get_client_configuration(customer_id):
    # pylint: disable-msg=W0703
    # pylint: disable-msg=W0613
    '''
    Here we are read client configuration from s3 bucket
    params - customer_id: client id
    '''
    client_config = {}
    # client_config = read_config_file_from_bucket(bucket_name, temp_path, default_config_path)
    try:
        client = redis.Redis(host='master.ewb-qa.xfl9sf.aps1.cache.amazonaws.com',\
            port=6379, db=0, ssl=True)
        get_data = client.get(customer_id + "_e-invoice_etl_cache")
        if get_data:
            client_config = orjson.loads(get_data)
    except Exception as error:
        LOGGER.error(str(error), exc_info=True)
    return client_config

def validate_req_body_structure(req_body, invoice_count, load_id=0):
    '''
        here we are validating request body structure and einvoice count
        params - req_body: request body
        params - invoice_count: total invoice count
        params - load_id: upload table load_id
    '''
    response_list = []
    # checking size
    if len(req_body) != invoice_count:
        error_dict = get_error("invoice count and request body count is not equal",\
            "invoice_count", "Error")
        response_body = copy.deepcopy(RESPONSE_STRUCTURE)
        response_body["pwc_response"]["message"] = RESPONSE_MESSAGE["INV_PLD_MI_MTCH_CNT"]
        response_body["pwc_response"]["status"] = STATUS_CODE["INV_PLD_MI_MTCH_CNT"]
        response_body["pwc_response"]["validation_remarks"].append(error_dict)
        response_body["pwc_response"]["validation_status"] = STATUS["ERROR"]
        if load_id:
            response_body["pwc_response"]["load_id"] = load_id
        response_list = [response_body]
    return response_list
