'''
All upload table functionality here
'''
import time
import datetime
import copy
import logging
import json
from settings.db_config import fetch_row, upload_insert_execute
from .upload_config import UPLOAD_STRUCTURE
from.query_configuration import UPLOAD_INSERT_QUERY
LOGGER = logging.getLogger("einvoice_app")

class Upload:
    '''
    upload table class
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
        print("Upload object")

    @staticmethod
    def get_load_id(cursor):
        '''
        Here we are fetching load_id from demo.upload table sequence
        params - customer_db: client database credential
        '''
        start_time = time.time()
        LOGGER.info("Start get_load_id")
        # query for load_id
        query = "select nextval('demo.upload_id_seq')"
        # get data from db
        data = fetch_row(cursor, query)
        LOGGER.info("End get_load_id, total time taken -> %s", format((\
            time.time() - start_time) * 1000, '.2f'))
        return data['nextval']

    @staticmethod
    def insert_load_id(req, req_body, response_body, load_id, conn, cursor,\
        database):
        '''
        Here we are making upload table data and inserting to upload table
        params - headers: request headers
        parmas - req_body: request body
        params - response_body: response body
        params - load_id: upload table load id
        params - database: client database credential
        '''
        start_time = time.time()
        LOGGER.info("Start insert_load_id")
        str_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        upload_data = copy.deepcopy(UPLOAD_STRUCTURE)
        upload_data["id"] = load_id
        upload_data["load_id"] = load_id
        upload_data["source_system"] = req.get_header("source_system", default='API')
        upload_data["data_type"] = req.get_header("data_type", default='einvoice')
        upload_data["load_type"] = req.get_header("load_type", default='SAP')
        upload_data["created_date"] = str_time
        upload_data["updated_date"] = str_time
        upload_data["einvoice_req_body"] = req_body.decode('utf-8')
        upload_data["einvoice_res_body"] = json.dumps(response_body)
        upload_insert_execute(upload_data, UPLOAD_INSERT_QUERY, conn, cursor, database)
        LOGGER.info("End insert_load_id, Total time taken - > %s", format(\
            (time.time() - start_time) * 1000, '.2f'))
