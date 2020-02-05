'''
Here we are creating data of irn_details table
'''
from .irn_details_config import IRN_DTLS_MPNG, IRN_DTLS_EXT_NODE, IRN_DTLS_DFLT

class IrnDetails:
    '''
    all irn_details releated functionaliry are here
    '''
    def __init__(self):
        '''
        initiate object
        '''
        pass

    def __str__(self):
        '''
        object representation
        '''
        print('IrnDetails object')

    @staticmethod
    def get_irn_details(payload, irn_dtls_list, created_date):
        '''
        Here we are extending irn_details data for insert
        params - payload: request body
        params - irn_dtls_list appending the data to irn_list
        params - created_date: create date
        '''
        irn_dtls_data = {}
        for ext_s_col, ext_t_col, ext_dflt in IRN_DTLS_DFLT:
            irn_dtls_data[ext_t_col] = payload.get(ext_s_col, ext_dflt)
        irn_dtls_data["il_created_date"] = created_date
        irn_dtls_data["il_updated_date"] = created_date
        # extracting line item
        for line_item in payload["ItemList"]:
            data = irn_dtls_data.copy()
            for s_col, t_col, dflt in IRN_DTLS_MPNG:
                data[t_col] = line_item.get(s_col, dflt)
            # child key extracting
            for key, value in IRN_DTLS_EXT_NODE.items():
                for config in value["columnList"]:
                    data[config['t_col']] = line_item.get(key, {}).get(\
                        config['s_col'], config['dflt'])
            irn_dtls_list.append(data)
