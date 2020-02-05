'''
Here we are creating data of irn_master table
'''
import datetime
import copy
import json
from jsonschema import Draft7Validator
from module.schema_validation.schema_configuration import SCHEMA
from .irn_master_config import IRN_MASTER_CONFIGURATION, IRN_MSTR_CMN_MPNG,\
    FL_IRN_MSTR_DFLT_DATA
from .irn_details import IrnDetails
from .irn_mis_details import IrnMisDetails

class IrnMaster:
    '''
    all irn master releated work are here
    '''
    def __init__(self):
        '''
        object initiated
        '''
        pass

    def __str__(self):
        '''
        object representation
        '''
        print('IrnMaster object')

    @staticmethod
    def map_default_value(payload, data):
        '''
            Here we are mapping data if key not found then set default value
            params - payload: request payload
        '''
        for cm_key, dflt_vl in IRN_MSTR_CMN_MPNG:
            data[cm_key] = payload.get(cm_key, dflt_vl)

    @staticmethod
    def map_res_body(irn_data, res_body):
        '''
        Here we are appending res_body
        params - irn_data: irn_master data
        params - res_body: response body
        '''
        irn_data['pwc_response_message'] = res_body.get('pwc_response', {}).get('message', '')
        irn_data['pwc_response_validation_status'] = res_body.get('pwc_response', {}).get(\
            'validation_status', '')
        pwc_res_v_rmrk = res_body.get('pwc_response', {}).get('validation_remarks')
        irn_data['pwc_response_validation_remarks'] = json.dumps(pwc_res_v_rmrk)
        irn_data['pwc_response_status'] = res_body.get('pwc_response', {}).get('status')

    @staticmethod
    def get_irn_master(payload, irn_list, irn_dtls_list, irn_mis_dtls_list, res_body):
        '''
        Here we are extending irn_master data for insert
        params - payload: request body
        params - irn_list appending the data to irn_list
        params - irn_dtls_list: line item data
        params - irn_mis_dtls_list: params - irn_mis_dtls_list appending the
            data to irn_mis_dtls_list
        params - res_body: fetch data from res_body for insertion
        '''
        irn_data = {}
        # fill response_body
        IrnMaster.map_res_body(irn_data, res_body)
        # extracting child key from parent node
        for key, value in IRN_MASTER_CONFIGURATION.items():
            for config in value["columnList"]:
                irn_data[config['t_col']] = payload.get(key, {}).get(\
                    config['s_col'], config['dflt'])
        # mapping value
        IrnMaster.map_default_value(payload, irn_data)

        crn_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        irn_data['created_date'] = crn_time
        irn_data["updated_date"] = crn_time
        irn_data["nic_request_payload"] = json.dumps(payload["nic_request_payload"]) if \
            "nic_request_payload" in payload else json.dumps(payload)
        irn_list.append(irn_data)
        # creating line item data
        IrnDetails.get_irn_details(payload, irn_dtls_list, crn_time)
        IrnMisDetails.get_irn_mis_details(payload, irn_mis_dtls_list, crn_time)

    @staticmethod
    def failure_data_irn_master(payload, irn_list, irn_dtls_list, irn_mis_dtls_list, res_body):
        '''
        Here we are extending irn_master data for insert
        params - payload: request body
        params - irn_list appending the data to irn_list
        params - irn_dtls_list: line item data
        params - irn_mis_dtls_list: params - irn_mis_dtls_list appending the
            data to irn_mis_dtls_list
        params - response body add to irn_master after schema validation failed
        '''
        validator = Draft7Validator(SCHEMA)
        errors = sorted(validator.iter_errors(payload), key=lambda e: e.path)

        message = [".".join(str(x) for x in error.relative_path) + "-" + \
            error.message + "<br>" for error in errors]
        if message:
            data = copy.deepcopy(FL_IRN_MSTR_DFLT_DATA)
            # fill response_body
            IrnMaster.map_res_body(data, res_body)
            IrnMaster.map_default_value(payload, data)
            crn_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            data['created_date'] = crn_time
            data["updated_date"] = crn_time
            data["nic_request_payload"] = json.dumps(payload["nic_request_payload"]) if \
                "nic_request_payload" in payload else json.dumps(payload)
            data["response_body"] = json.dumps(res_body)
            data["validation_remark"] = message
            irn_list.append(data)
        else:
            IrnMaster.get_irn_master(payload, irn_list, irn_dtls_list, irn_mis_dtls_list, res_body)
