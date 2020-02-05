'''
Here we are parsing json to csv for ewb
'''
import copy
import logging
from .configuration import EWB_STRUCTURE_PAYLOAD, MAND_DATA_MAPPING, MAND_ITM_LVL_MAPPING,\
    UNIT_CONFIG, STATE_CONFIG, STATE_TRANSFORMATION_LIST, DOC_TYPE_CONFIG, TRAN_TYPE_CONFIG,\
    DFLT_VAL_MAP
LOGGER = logging.getLogger("einvoice_app")


class EwbParse:
    '''
        Here we are transforming einvoice data into ewb data
    '''
    def __init__(self):
        '''
        object initiate
        '''
        pass

    def __str__(self):
        '''
        obect representation
        '''
        print("EwbParse object")

    @staticmethod
    def ewb_json_csv_parse(payload, ewb_list):
        '''
            Here we are parsing einvoice json to ewb_details structure and
            create csv
            params - payload: einvoice payload
            params - ewb_list: appending transform data to ewb_list
        '''
        ewb_data = copy.deepcopy(EWB_STRUCTURE_PAYLOAD)

        # get user gstin
        gstin = payload.get('User_GSTIN')
        if not gstin:
            gstin = payload.get('SellerDtls', {}).get('Gstin', '')
        ewb_data['User GSTIN'] = gstin
        # Here we are mapping invoice level data
        for key in MAND_DATA_MAPPING:
            if key in payload:
                for einvoice_key, ewb_key, dflt_val in MAND_DATA_MAPPING[key]:
                    ewb_data[ewb_key] = payload[key].get(einvoice_key, dflt_val)
        # einvoice data map
        for ei_key, ew_key, ew_dflt_val in DFLT_VAL_MAP:
            ewb_data[ew_key] = payload.get(ei_key, ew_dflt_val)
        # UNIT Transformation
        ewb_data["Unit"] = UNIT_CONFIG[ewb_data["Unit"]] if \
            ewb_data["Unit"] in UNIT_CONFIG else ewb_data["Unit"]
        # Document Type Transformation
        upr_doc_type = ewb_data["Document Type"].upper()
        ewb_data["Document Type"] = DOC_TYPE_CONFIG[upr_doc_type] if \
            upr_doc_type in DOC_TYPE_CONFIG else ewb_data["Document Type"]
        # Transaction Type Transformation
        upr_fu6 = ewb_data["FU 6"].upper()
        ewb_data["FU 6"] = TRAN_TYPE_CONFIG[upr_fu6] if \
            upr_fu6 in TRAN_TYPE_CONFIG else ewb_data["FU 6"]
        # STATE TRANSFROMATION
        for state in STATE_TRANSFORMATION_LIST:
            ewb_data[state] = STATE_CONFIG[ewb_data[state]] if \
                ewb_data[state] in STATE_CONFIG else ewb_data[state]
        # start mapping line item data
        count = 1
        for line_item in payload["ItemList"]:
            cp_ewb_data = copy.deepcopy(ewb_data)
            for e_inv_itm_key, ewb_item_key, itm_dflt_val in MAND_ITM_LVL_MAPPING:
                cp_ewb_data[ewb_item_key] = line_item.get(e_inv_itm_key, itm_dflt_val)
            cp_ewb_data["Line Item"] = count
            count += 1
            ewb_list.append(cp_ewb_data)
