'''
all transformation releated work are here
'''
import os
from jsonschema import Draft7Validator
from settings.configuration import RESPONSE_MESSAGE
from settings.redis_cache import RedisCache
from module.schema_validation.schema_configuration import GST_AMT_CHCK_SCHEMA, GST_RT_CHCK_SCHEMA
class TransformData:
    '''
    transforming data
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
        print("TransformData object")

    @staticmethod
    def transform_mis(payload, configuration, res_body, customer_id):
        '''
        transforming columns
        params - payload: request body
        params - configuration: client configuration
        params - res_body: response body
        params - customer_id: cleint id
        '''
        env = os.environ.get("env", "qa")
        mstr_data = RedisCache.get_master_config(customer_id, env)
        # mstr_data = configuration.get('master_config')
        if mstr_data:
            upr_gstin = payload.get('SellerDtls', {}).get('Gstin', "").upper()
            flag_gstin = upr_gstin in mstr_data["company_master"]
            gstin_id = "-1"
            company_id = "-1"

            if flag_gstin:
                company_id = str(mstr_data["company_master"][upr_gstin][0])
                company_name = mstr_data["company_master"][upr_gstin][1]
                gstin_id = mstr_data["company_master"][upr_gstin][2]

            upr_bu = payload.get('MisColumns', {}).get('Bu', '').upper()
            bu_id = '0'
            if upr_bu:
                key_bu = f"{company_id}:{upr_bu}"
                #Checking if the bu concatenated with company_id is present in master data
                flag_bu = key_bu in mstr_data["bu_master"]
                if flag_bu:
                    bu_id = mstr_data["bu_master"][key_bu]
                else:
                    payload["bu_flag"] = True

            sbu_id = '0'
            upr_sbu = payload.get('MisColumns', {}).get('Sbu', '').upper()
            if upr_sbu:
                key_sbu = f"{company_id}:{upr_sbu}:{upr_bu}"
                #Checking if the bu concatenated with company_id is present in master data
                flag_sbu = key_sbu in mstr_data["sbu_master"]
                if flag_sbu:
                    sbu_id = mstr_data["sbu_master"][key_sbu]
                else:
                    payload["sbu_flag"] = True

            loc_id = '0'
            upr_loc = payload.get('MisColumns', {}).get('Location', '').upper()
            if upr_loc:
                key_loc = f"{company_id}:{upr_loc}"
                if key_loc:
                    flag_loc = key_loc in mstr_data["location_master"]
                    if flag_loc:
                        loc_id = mstr_data['location_master'][key_loc]
                    else:
                        payload["loc_flag"] = True

            payload['bu_id'] = bu_id
            payload['gstin_id'] = gstin_id
            payload['company_id'] = company_id
            payload['sbu_id'] = sbu_id
            payload['location_id'] = loc_id
        else:
            res_body["pwc_response"]["message"] += f", {RESPONSE_MESSAGE['MSTR_CNFG_MSNG']}"

class ValDtlsTransform:
    '''
    Here Transforming Valdtls node
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
        print("ValDtlsTransform object")

    @staticmethod
    def gstamount_transform(payload, valdtls):
        '''
            here creating valdtls node
            params - payload: request payload
            params - valdtls: valdtls node
        '''
        for item in payload["ItemList"]:
            valdtls['CgstVal'] += item.get('CgstAmt', 0)
            valdtls['SgstVal'] += item.get('SgstAmt', 0)
            valdtls['IgstVal'] += item.get('IgstAmt', 0)
            valdtls['CesVal'] += item.get('CessAmt', 0)
            valdtls['AssVal'] += item.get('AssAmt', 0)
            valdtls['StCesVal'] += item.get('StateCes', 0)
            valdtls['CesNonAdVal'] += item.get('CesNonAdVal', 0)
            valdtls['TotInvVal'] += item.get('TotItemVal', 0)

        payload['ValDtls'] = valdtls

    @staticmethod
    def get_percentage_amount(item, key, assamt):
        '''
        here we are getting percentage amount
        params - item: line item
        params - key: gst rate
        params - assAmt: Assessment amount
        '''
        perc_amount = 0
        rate = item.get(key, 0)
        if rate:
            perc_amount = assamt * rate / 100
            perc_amount = float(format(perc_amount, '.2f'))
        return perc_amount

    @staticmethod
    def gstrate_transform(payload, valdtls):
        '''
            here creating valdtls node
            params - payload: request payload
            params - valdtls: valdtls node
        '''
        for item in payload["ItemList"]:
            assamt = item.get('AssAmt', 0)
            if assamt:
                valdtls['CgstVal'] += ValDtlsTransform.get_percentage_amount(\
                    item, 'CgstRt', assamt)
                valdtls['SgstVal'] += ValDtlsTransform.get_percentage_amount(\
                    item, 'SgstRt', assamt)
                valdtls['IgstVal'] += ValDtlsTransform.get_percentage_amount(\
                    item, 'IgstRt', assamt)
                valdtls['CesVal'] += ValDtlsTransform.get_percentage_amount(\
                    item, 'CesRt', assamt)
                valdtls['AssVal'] += item.get('AssAmt', 0)
            valdtls['StCesVal'] += item.get('StateCes', 0)
            valdtls['CesNonAdVal'] += item.get('CesNonAdVal', 0)
            valdtls['TotInvVal'] += item.get('TotItemVal', 0)
        payload['ValDtls'] = valdtls

    @staticmethod
    def transform_valdtls(payload):
        '''
        Here we are transforming valdtls
        if valdtls does not exist in payload then calculate total sum
        individual mandatory field from ItemList node
        params - payload: request payload
        '''
        valdtls = {"AssVal": 0,\
            "CgstVal": 0,\
            "SgstVal": 0,\
            "IgstVal": 0,\
            "CesVal": 0,\
            "StCesVal": 0,\
            "CesNonAdVal": 0,\
            "TotInvVal": 0,\
        }
        # can we need to validate ItemList payload for this field ??
        # question is how to calculate
        # cgstVal, SgstVal, IgstVal, CesVal, StCesVal, CesNonAdval, TotInvVal
        # cgstval = AssAmt * CgstRt /100
        # sgstval = AssAmt * SgstRt /100
        # igstval = AssAmt * IgstRt /100
        # cesval = AssAmt * CesRt /100
        # CesNonAdVal = sum
        # StCesVal = Sum
        # TotInvVal = (cgstVal, SgstVal, IgstVal, CesVal, StCesVal, CesNonAdval) sum
        if "ItemList" in payload and "ValDtls" not in payload:
            # 1st check gst amount exist or not
            validator = Draft7Validator(GST_AMT_CHCK_SCHEMA)
            errors = sorted(validator.iter_errors(payload), key=lambda e: e.path)
            if not errors:
                # transforming data
                ValDtlsTransform.gstamount_transform(payload, valdtls)
            else:
                validator = Draft7Validator(GST_RT_CHCK_SCHEMA)
                errors = sorted(validator.iter_errors(payload), key=lambda e: e.path)
                if not errors:
                    # transformaing gstrate data
                    ValDtlsTransform.gstrate_transform(payload, valdtls)
