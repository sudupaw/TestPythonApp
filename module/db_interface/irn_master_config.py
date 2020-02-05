'''
Here We are configure table mapping
'''
FL_IRN_MSTR_DFLT_DATA = {'trandtls_outwardinward': '', 'trandtls_subtype': '',\
    'trandtls_subtypedescription': '', 'trandtls_catg': '', 'trandtls_regrev': '',\
    'trandtls_typ': '', 'trandtls_ecmtrn': '', 'trandtls_ecmgstin': '', 'trandtls_pos': 0,\
    'trandtls_claimingrefund': '', 'trandtls_diffpercentage': '', 'trandtls_taxability': '',\
    'trandtls_interintra': '', 'docdtls_typ': '', 'docdtls_no': '', 'docdtls_dt': None,\
    'docdtls_orginvno': '', 'docdtls_orginvdt': None, 'docdtls_reasonforcndn': '',\
    'sellerdtls_gstin': '', 'sellerdtls_trdnm': '', 'sellerdtls_bno': '', 'sellerdtls_bnm': '',\
    'sellerdtls_flno': '', 'sellerdtls_loc': '', 'sellerdtls_dst': '', 'sellerdtls_pin': 0,\
    'sellerdtls_stcd': 0, 'sellerdtls_ph': 0, 'sellerdtls_em': '', 'sellerdtls_suppliercode': '',\
    'buyerdtls_gstin': '', 'buyerdtls_trdnm': '', 'buyerdtls_bno': '', 'buyerdtls_bnm': '',\
    'buyerdtls_flno': '', 'buyerdtls_loc': '', 'buyerdtls_dst': '', 'buyerdtls_pin': 0,\
    'buyerdtls_stcd': 0, 'buyerdtls_ph': 0, 'buyerdtls_em': '', 'buyerdtls_customercode': '',\
    'dispdtls_gstin': '', 'dispdtls_trdnm': '', 'dispdtls_bno': '', 'dispdtls_bnm': '',\
    'dispdtls_flno': '', 'dispdtls_loc': '', 'dispdtls_dst': '', 'dispdtls_pin': 0,\
    'dispdtls_stcd': 0, 'dispdtls_ph': 0, 'dispdtls_em': '', 'shipdtls_gstin': '',\
    'shipdtls_trdnm': '', 'shipdtls_bno': '', 'shipdtls_bnm': '', 'shipdtls_flno': '',\
    'shipdtls_loc': '', 'shipdtls_dst': '', 'shipdtls_pin': 0, 'shipdtls_stcd': 0,\
    'shipdtls_ph': 0, 'shipdtls_em': '', 'valdtls_assval': 0, 'valdtls_cgstval': 0,\
    'valdtls_sgstval': 0, 'valdtls_igstval': 0, 'valdtls_cesval': 0, 'valdtls_stcesval': 0,\
    'valdtls_cesnonadval': 0, 'valdtls_disc': 0, 'valdtls_othchrg': 0, 'valdtls_totinvval': 0,\
    'paydtls_nam': '', 'paydtls_mode': '', 'paydtls_fininsbr': '', 'paydtls_payterm': '',\
    'paydtls_payinstr': '', 'paydtls_crtrn': '', 'paydtls_dirdr': '', 'paydtls_crday': 0,\
    'paydtls_balamt': 0, 'paydtls_payduedt': None, 'paydtls_acctdet': '', 'refdtls_invrmk': '',\
    'refdtls_invstdt': None, 'refdtls_invenddt': None, 'refdtls_precinvno': '',\
    'refdtls_precinvdt': None, 'refdtls_recadvref': '', 'refdtls_tendref': '',\
    'refdtls_contrref': '', 'refdtls_extref': '', 'refdtls_projref': '', 'refdtls_poref': '',\
    'refdtls_vendorporefdt': None, 'refdtls_accountingdocno': '', 'refdtls_accountingdocdt': None,\
    'refdtls_sono': '', 'refdtls_sodt': None, 'expdtls_expcat': '', 'expdtls_wthpay': '',\
    'expdtls_shipbno': '', 'expdtls_shipbdt': None, 'expdtls_port': '', 'expdtls_invforcur': 0,\
    'expdtls_forcur': '', 'expdtls_cntcode': '', 'transportdtls_transporterid': '',\
    'transportdtls_distancekm': 0, 'transportdtls_transportername': '',\
    'transportdtls_transmode': '', 'transportdtls_transdocno': '',\
    'transportdtls_transdocdate': None, 'transportdtls_vehicleno': '',\
    'transportdtls_vehicletype': '', 'bu': '', 'sbu': '', 'location': '', 'user': '',\
    'companycode': '', 'companyname': '', 'trackingno': '', 'transactioncount': 0,\
    'glaccount': '', 'ewbno': None, 'returnperiod': '',\
}
IRN_MASTER_CONFIGURATION = {\
    "TranDtls": {\
        "columnList": [\
            {"s_col": "OutwardInward", "t_col": "trandtls_outwardinward", "dflt": ""},\
            {"s_col": "SubType", "t_col": "trandtls_subtype", "dflt": ""},\
            {"s_col": "SubTypeDescription", "t_col": "trandtls_subtypedescription", "dflt": ""},\
            {"s_col": "Catg", "t_col": "trandtls_catg", "dflt": ""},\
            {"s_col": "RegRev", "t_col": "trandtls_regrev", "dflt": ""},\
            {"s_col": "Typ", "t_col": "trandtls_typ", "dflt": ""},\
            {"s_col": "EcmTrn", "t_col": "trandtls_ecmtrn", "dflt": ""},\
            {"s_col": "EcmGstin", "t_col": "trandtls_ecmgstin", "dflt": ""},\
            {"s_col": "Pos", "t_col": "trandtls_pos", "dflt": 0},\
            {"s_col": "ClaimingRefund", "t_col": "trandtls_claimingrefund", "dflt": ""},\
            {"s_col": "DiffPercentage", "t_col": "trandtls_diffpercentage", "dflt": ""},\
            {"s_col": "Taxability", "t_col": "trandtls_taxability", "dflt": ""},\
            {"s_col": "InterIntra", "t_col": "trandtls_interintra", "dflt": ""},\
        ],\
    },
    "DocDtls": {\
        "columnList": [\
            {"s_col": "Typ", "t_col": "docdtls_typ", "dflt": ""},\
            {"s_col": "No", "t_col": "docdtls_no", "dflt": ""},\
            {"s_col": "Dt", "t_col": "docdtls_dt", "dflt": None},\
            {"s_col": "OrgInvNo", "t_col": "docdtls_orginvno", "dflt": ""},\
            {"s_col": "OrgInvDt", "t_col": "docdtls_orginvdt", "dflt": None},\
            {"s_col": "ReasonForCnDn", "t_col": "docdtls_reasonforcndn", "dflt": ""},\
        ],\
    },\
    "SellerDtls": {\
        "columnList": [\
            {"s_col": "Gstin", "t_col": "sellerdtls_gstin", "dflt": ""},\
            {"s_col": "TrdNm", "t_col": "sellerdtls_trdnm", "dflt": ""},\
            {"s_col": "Bno", "t_col": "sellerdtls_bno", "dflt": ""},\
            {"s_col": "Bnm", "t_col": "sellerdtls_bnm", "dflt": ""},\
            {"s_col": "Flno", "t_col": "sellerdtls_flno", "dflt": ""},\
            {"s_col": "Loc", "t_col": "sellerdtls_loc", "dflt": ""},\
            {"s_col": "Dst", "t_col": "sellerdtls_dst", "dflt": ""},\
            {"s_col": "Pin", "t_col": "sellerdtls_pin", "dflt": 0},\
            {"s_col": "Stcd", "t_col": "sellerdtls_stcd", "dflt": 0},\
            {"s_col": "Ph", "t_col": "sellerdtls_ph", "dflt": 0},\
            {"s_col": "Em", "t_col": "sellerdtls_em", "dflt": ""},\
            {"s_col": "SupplierCode", "t_col": "sellerdtls_suppliercode", "dflt": ""},\
        ],\
    },\
    "BuyerDtls": {\
        "columnList": [\
            {"s_col": "Gstin", "t_col": "buyerdtls_gstin", "dflt": ""},\
            {"s_col": "TrdNm", "t_col": "buyerdtls_trdnm", "dflt": ""},\
            {"s_col": "Bno", "t_col": "buyerdtls_bno", "dflt": ""},\
            {"s_col": "Bnm", "t_col": "buyerdtls_bnm", "dflt": ""},\
            {"s_col": "Flno", "t_col": "buyerdtls_flno", "dflt": ""},\
            {"s_col": "Loc", "t_col": "buyerdtls_loc", "dflt": ""},\
            {"s_col": "Dst", "t_col": "buyerdtls_dst", "dflt": ""},\
            {"s_col": "Pin", "t_col": "buyerdtls_pin", "dflt": 0},\
            {"s_col": "Stcd", "t_col": "buyerdtls_stcd", "dflt": 0},\
            {"s_col": "Ph", "t_col": "buyerdtls_ph", "dflt": 0},\
            {"s_col": "Em", "t_col": "buyerdtls_em", "dflt": ""},\
            {"s_col": "CustomerCode", "t_col": "buyerdtls_customercode", "dflt": ""},\
        ],\
    },\
    "DispDtls": {\
        "columnList": [\
            {"s_col": "Gstin", "t_col": "dispdtls_gstin", "dflt": ""},\
            {"s_col": "TrdNm", "t_col": "dispdtls_trdnm", "dflt": ""},\
            {"s_col": "Bno", "t_col": "dispdtls_bno", "dflt": ""},\
            {"s_col": "Bnm", "t_col": "dispdtls_bnm", "dflt": ""},\
            {"s_col": "Flno", "t_col": "dispdtls_flno", "dflt": ""},\
            {"s_col": "Loc", "t_col": "dispdtls_loc", "dflt": ""},\
            {"s_col": "Dst", "t_col": "dispdtls_dst", "dflt": ""},\
            {"s_col": "Pin", "t_col": "dispdtls_pin", "dflt": 0},\
            {"s_col": "Stcd", "t_col": "dispdtls_stcd", "dflt": 0},\
            {"s_col": "Ph", "t_col": "dispdtls_ph", "dflt": 0},\
            {"s_col": "Em", "t_col": "dispdtls_em", "dflt": ""},\
        ],\
    },\
    "ShipDtls": {\
        "columnList": [\
            {"s_col": "Gstin", "t_col": "shipdtls_gstin", "dflt": ""},\
            {"s_col": "TrdNm", "t_col": "shipdtls_trdnm", "dflt": ""},\
            {"s_col": "Bno", "t_col": "shipdtls_bno", "dflt": ""},\
            {"s_col": "Bnm", "t_col": "shipdtls_bnm", "dflt": ""},\
            {"s_col": "Flno", "t_col": "shipdtls_flno", "dflt": ""},\
            {"s_col": "Loc", "t_col": "shipdtls_loc", "dflt": ""},\
            {"s_col": "Dst", "t_col": "shipdtls_dst", "dflt": ""},\
            {"s_col": "Pin", "t_col": "shipdtls_pin", "dflt": 0},\
            {"s_col": "Stcd", "t_col": "shipdtls_stcd", "dflt": 0},\
            {"s_col": "Ph", "t_col": "shipdtls_ph", "dflt": 0},\
            {"s_col": "Em", "t_col": "shipdtls_em", "dflt": ""},\
        ],\
    },\
    "ValDtls": {\
        "columnList": [\
            {"s_col": "AssVal", "t_col": "valdtls_assval", "dflt": 0},\
            {"s_col": "CgstVal", "t_col": "valdtls_cgstval", "dflt": 0},\
            {"s_col": "SgstVal", "t_col": "valdtls_sgstval", "dflt": 0},\
            {"s_col": "IgstVal", "t_col": "valdtls_igstval", "dflt": 0},\
            {"s_col": "CesVal", "t_col": "valdtls_cesval", "dflt": 0},\
            {"s_col": "StCesVal", "t_col": "valdtls_stcesval", "dflt": 0},\
            {"s_col": "CesNonAdVal", "t_col": "valdtls_cesnonadval", "dflt": 0},\
            {"s_col": "Disc", "t_col": "valdtls_disc", "dflt": 0},\
            {"s_col": "OthChrg", "t_col": "valdtls_othchrg", "dflt": 0},\
            {"s_col": "TotInvVal", "t_col": "valdtls_totinvval", "dflt": 0},\
        ],\
    },\
    "PayDtls": {\
        "columnList": [\
            {"s_col": "Nam", "t_col": "paydtls_nam", "dflt": ""},\
            {"s_col": "Mode", "t_col": "paydtls_mode", "dflt": ""},\
            {"s_col": "FinInsBr", "t_col": "paydtls_fininsbr", "dflt": ""},\
            {"s_col": "PayTerm", "t_col": "paydtls_payterm", "dflt": ""},\
            {"s_col": "PayInstr", "t_col": "paydtls_payinstr", "dflt": ""},\
            {"s_col": "CrTrn", "t_col": "paydtls_crtrn", "dflt": ""},\
            {"s_col": "DirDr", "t_col": "paydtls_dirdr", "dflt": ""},\
            {"s_col": "CrDay", "t_col": "paydtls_crday", "dflt": 0},\
            {"s_col": "BalAmt", "t_col": "paydtls_balamt", "dflt": 0},\
            {"s_col": "PayDueDt", "t_col": "paydtls_payduedt", "dflt": None},\
            {"s_col": "AcctDet", "t_col": "paydtls_acctdet", "dflt": ""},\
        ],\
    },\
    "RefDtls": {\
        "columnList": [\
            {"s_col": "InvRmk", "t_col": "refdtls_invrmk", "dflt": ""},\
            {"s_col": "InvStDt", "t_col": "refdtls_invstdt", "dflt": None},\
            {"s_col": "InvEndDt", "t_col": "refdtls_invenddt", "dflt": None},\
            {"s_col": "PrecInvNo", "t_col": "refdtls_precinvno", "dflt": ""},\
            {"s_col": "PrecInvDt", "t_col": "refdtls_precinvdt", "dflt": None},\
            {"s_col": "RecAdvRef", "t_col": "refdtls_recadvref", "dflt": ""},\
            {"s_col": "TendRef", "t_col": "refdtls_tendref", "dflt": ""},\
            {"s_col": "ContrRef", "t_col": "refdtls_contrref", "dflt": ""},\
            {"s_col": "ExtRef", "t_col": "refdtls_extref", "dflt": ""},\
            {"s_col": "ProjRef", "t_col": "refdtls_projref", "dflt": ""},\
            {"s_col": "PORef", "t_col": "refdtls_poref", "dflt": ""},\
            {"s_col": "VendorPoRefDt", "t_col": "refdtls_vendorporefdt", "dflt": None},\
            {"s_col": "AccountingDocNo", "t_col": "refdtls_accountingdocno", "dflt": ""},\
            {"s_col": "AccountingDocDt", "t_col": "refdtls_accountingdocdt", "dflt": None},\
            {"s_col": "SoNo", "t_col": "refdtls_sono", "dflt": ""},\
            {"s_col": "SoDt", "t_col": "refdtls_sodt", "dflt": None},\
        ],\
    },\
    "ExpDtls": {\
        "columnList": [\
            {"s_col": "ExpCat", "t_col": "expdtls_expcat", "dflt": ""},\
            {"s_col": "WthPay", "t_col": "expdtls_wthpay", "dflt": ""},\
            {"s_col": "ShipBNo", "t_col": "expdtls_shipbno", "dflt": ""},\
            {"s_col": "ShipBDt", "t_col": "expdtls_shipbdt", "dflt": None},\
            {"s_col": "Port", "t_col": "expdtls_port", "dflt": ""},\
            {"s_col": "InvForCur", "t_col": "expdtls_invforcur", "dflt": 0},\
            {"s_col": "ForCur", "t_col": "expdtls_forcur", "dflt": ""},\
            {"s_col": "CntCode", "t_col": "expdtls_cntcode", "dflt": ""},\
        ],\
    },\
    "TransportDtls": {\
        "columnList": [\
            {"s_col": "TransporterId", "t_col": "transportdtls_transporterid", "dflt": ""},\
            {"s_col": "DistanceKm", "t_col": "transportdtls_distancekm", "dflt": 0},\
            {"s_col": "TransporterName", "t_col": "transportdtls_transportername", "dflt": ""},\
            {"s_col": "TransMode", "t_col": "transportdtls_transmode", "dflt": ""},\
            {"s_col": "TransDocNo", "t_col": "transportdtls_transdocno", "dflt": ""},\
            {"s_col": "TransDocDate", "t_col": "transportdtls_transdocdate", "dflt": None},\
            {"s_col": "VehicleNo", "t_col": "transportdtls_vehicleno", "dflt": ""},\
            {"s_col": "VehicleType", "t_col": "transportdtls_vehicletype", "dflt": ""},\
        ],\
    },\
    "MisColumns": {\
        "columnList": [\
            {"s_col": "Bu", "t_col": "bu", "dflt": ""},\
            {"s_col": "Sbu", "t_col": "sbu", "dflt": ""},\
            {"s_col": "Location", "t_col": "location", "dflt": ""},\
            {"s_col": "User", "t_col": "user", "dflt": ""},\
            {"s_col": "CompanyCode", "t_col": "companycode", "dflt": ""},\
            {"s_col": "CompanyName", "t_col": "companyname", "dflt": ""},\
            {"s_col": "TrackingNo", "t_col": "trackingno", "dflt": ""},\
            {"s_col": "TransactionCount", "t_col": "transactioncount", "dflt": 0},\
            {"s_col": "GlAccount", "t_col": "glaccount", "dflt": ""},\
            {"s_col": "EwbNo", "t_col": "ewbno", "dflt": None},\
            {"s_col": "ReturnPeriod", "t_col": "returnperiod", "dflt": ""},\
        ],\
    },\
}
# common get
IRN_MSTR_CMN_MPNG = [\
    ("is_irn", ""),\
    ("is_ewb", ""),\
    ("is_cancel", ""),\
    ("mis_action", ""),\
    ("nic_header", ""),\
    ("nic_status", ""),\
    ("nic_gen_mode", ""),\
    ("nic_document_status_created_date", None),\
    ("nic_response_encoded", ""),\
    ("nic_response_plaintext_json", ""),\
    ("nic_response_created_date", None),\
    ("nic_response_status", ""),\
    ("nic_response_errorcode", None),\
    ("ackno", None),\
    ("ackdt", None),\
    ("signedinvoice", ""),\
    ("signedqrcode", ""),\
    ("created_by", "System"),\
    ("updated_by", "System"),\
    ("is_active", "Y"),\
    ("data_source", "API"),\
    ("comments", ""),\
    ("update_history", ""),\
    ("load_id", 0),\
    ("udid", ""),\
    ("bu_id", 0),\
    ("sbu_id", 0),\
    ("location_id", 0),\
    ("gstin_id", 0),\
    ("company_id", 0),\
    ("user_gstin", ""),\
    ("irn", ""),\
    ("response_body", ""),\
    ("validation_remark", ""),\
    ("is_exclude", "N"),\
    ('nic_error_details', ''),\
    ('nic_qr_image', ''),\
    ('report_url', ''),\
    ('irp_response_message', ''),\
    ('irp_response_error', None),\
    ('irn_status', 'Pending'),\
    ('exclude_reason', ""),\
]
