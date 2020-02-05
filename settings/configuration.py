'''
ALL CONFIGURATIONS ARE HERE
'''
RESPONSE_STRUCTURE = {
        "pwc_response": {"invoice_number": "",\
        "gstin": "",\
        "document_date": "",\
        "document_type": "",\
        "status": "",\
        "message": "",\
        "validation_status": "",\
        "validation_remarks": [],\
    }
}
# STATUS CODE
STATUS_CODE = {"AUTH_FAILED": 701, "SCH_VAL_FAILED": 702,\
    "BSN_VAL_FAILED": 703, "SUCCESS": 700, "EXCEPTION": 705, "CONFIG_MISSING": 706,\
    "INV_PLD_MI_MTCH_CNT": 707}
# RESPONSE MESSAGE STRUCTURE
RESPONSE_MESSAGE = {"AUTH_FAILED": "PwC Authentication Failed",\
    "AUTH_PASSED": "PwC Authentication Passed",\
    "SCH_VAL_FAILED": "PwC Schema Validation Failed",\
    "SCH_VAL_PASSED": "PwC Schema Validation Passed",\
    "BSN_VAL_FAILED": "PwC Business Validation Failed",\
    "BSN_VAL_PASSED": "PwC Business Validation Passed",\
    "INV_PLD_MI_MTCH_CNT": "Invoice Payload Count Mismatch",\
    "VAL_NT_REQ": "PwC Schema & Business Validation Not Required",\
    "IRP_GEN_FAILED": "IRP Generation Failed",\
    "IPR_GEN_PASSED": "IRP Generated",\
    "IRN_DETERMINE": "Set is_irn",\
    "IRP_FLAG_FALSE": "IRP Flag is False",\
    "IS_IRN_NOT_REQUIRD": "IRP Not Required",\
    "MSTR_CNFG_MSNG": "Master Config Missing",\
    "IRN_FAILED": "Generation Failed",\
    "IRN_SUCCESS": "Generated",\
    "IRN_EXC_RSN": "IRN Excluded",\
}
# SET FLAG STATUS
FLAG = {"YES": "Y", "NO": "N"}
# STATUS
STATUS = {"ERROR": "Error", "SUCCESS": "Success", "ALERT": "Alert"}
# save required
SAVE_REQUIRED = [703, 700]
# PROCESS NAME
PROCESS_NAME = {"IRN_GENERATE": "IRN GENERATE"}
# SQS TEMPLATE
SQS_TEMPLATE = {"AUTH_FAILED": "Authentication Failed",\
    "SCH_VAL_FAILED": "Schema Validation Failed",\
    "BSN_VAL_FAILED": "Business Validation Failed",\
    "IRP_GEN_FAILED": "IRP Generation Failed",\
    "IPR_GEN_PASSED": "IRP Genereated",\
    "NIC_ERROR": "NIC Error Occured",\
    "EXCEPTION": "System Exception",\
}
# ERROR MESSAGE DICT
ERROR_MESSAGE_CONFIG = {"token": "token is missing in header",\
    "customer_id": "customer_id is missing in header",\
    "customer_id_int": "customer_id must be integer",\
    "req_body_required": "request body is required",\
    "req_body_invalid": "request body is not valid",\
    "customer_invalid": "Token/customer_id is invalid",\
    "schema_invalid": "error in payload",\
    "schema_valid": "payload is correct"}
# TRANS DETAILS CATAGORY CONFIGURATION LIST
TRANS_DTLS_CAT_LIST = ("B2B", "B2G", "EXP", "b2b", "b2g", "exp")
# DOCUMENT TYPES CONFIGURATION LIST
DOC_DTLS_TYPE_LIST = ("INV", "CRN", "DBN", "inv", "crn", "dbn")
# CLIENT CONFIGURATION FILE NAME
CLIENT_CONFIGURATION = "client_configuration.json"
# Financial START MONTH
FIN_STRT_MNTH = 4
# Extra field appending in response body
EXTRA_FIELD_APPEND = {
    "udid": "",\
    "is_irn": "N",\
    "is_exclude": "N",\
    "load_id": 0,\
    "is_ewb": "N",\
}
# Redis configuration read
REDIS_CONFIG = {
    "dev":{},\
    "qa": {"host": "master.ewb-qa.xfl9sf.aps1.cache.amazonaws.com", "port": 6379, "db": 0},\
    "prod": {},\
}
