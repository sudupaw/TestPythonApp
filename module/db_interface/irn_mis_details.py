'''
Here we are creating data of irn_mis_details table
'''
from .irn_mis_details_config import IRN_MIS_DTLS_MPNG, IRN_MIS_DTLS_DFLT

class IrnMisDetails:
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
        print('IrnMisDetails object')

    @staticmethod
    def get_irn_mis_details(payload, irn_mis_dtls_list, created_date):
        '''
        Here we are extending irn_mis_details data for insert
        params - payload: request body
        params - irn_mis_dtls_list appending the data to irn_mis_dtls_list
        params - created_date: create date
        '''
        data = {}
        # Mapping columns
        for key, value in IRN_MIS_DTLS_MPNG.items():
            for config in value["columnList"]:
                data[config['t_col']] = payload.get(key, {}).get(\
                    config['s_col'], config['dflt'])
        # map
        for ext_key, ext_dflt in IRN_MIS_DTLS_DFLT:
            data[ext_key] = payload.get(ext_key, ext_dflt)
        # date map
        data["created_date"] = created_date
        data["updated_date"] = created_date
        # append
        irn_mis_dtls_list.append(data)
