'''
irn details config
'''
IRN_DTLS_MPNG = [('LineItem', 'il_lineitem', 0),\
    ('ItemCode', 'il_itemcode', ''),\
    ('PrdNm', 'il_prdnm', ''),\
    ('PrdDesc', 'il_prddesc', ''),\
    ('HsnCd', 'il_hsncd', ''),\
    ('GoodsService', 'il_goodsservice', ''),\
    ('BarCde', 'il_barcde', ''),\
    ('Qty', 'il_qty', 0),\
    ('FreeQty', 'il_freeqty', 0),\
    ('Unit', 'il_unit', ''),\
    ('UnitPrice', 'il_unitprice', 0),\
    ('TotAmt', 'il_totamt', 0),\
    ('CgstRt', 'il_cgstrt', 0),\
    ('SgstRt', 'il_sgstrt', 0),\
    ('IgstRt', 'il_igstrt', 0),\
    ('CesRt', 'il_cesrt', 0),\
    ('CesNonAdVal', 'il_cesnonadval', 0),\
    ('StateCes', 'il_stateces', 0),\
    ('TotItemVal', 'il_totitemval', 0),\
    ('Discount', 'il_discount', 0),\
    ('OthChrg', 'il_othchrg', 0),\
    ('Vat', 'il_vat', 0),\
    ('CentralExcise', 'il_centralexcise', 0),\
    ('StateExcise', 'il_stateexcise', 0),\
    ('ExportDuty', 'il_exportduty', 0),\
    ('ValueBeforeBcd', 'il_valuebeforebcd', 0),\
    ('Bcd', 'il_bcd', 0),\
    ('AssAmt', 'il_assamt', 0),\
    ('TotalGstRate', 'il_totalgstrate', 0),\
    ('CessNonAdvolRt', 'il_cessnonadvolrt', 0),\
    ('IgstAmt', 'il_igstamt', 0),\
    ('CgstAmt', 'il_cgstamt', 0),\
    ('SgstAmt', 'il_sgstamt', 0),\
    ('CessAmt', 'il_cessamt', 0),\
    ('EligibilityItc', 'il_eligibilityitc', ''),\
    ('ItcIgst', 'il_itcigst', 0),\
    ('ItcCgst', 'il_itccgst', 0),\
    ('ItcSgst', 'il_itcsgst', 0),\
    ('ItcCess', 'il_itccess', 0),\
    ('NatureOfExpense', 'il_natureofexpense', ''),\
    ('Mis1', 'il_mis1', ''),\
    ('Mis2', 'il_mis2', ''),\
    ('Mis3', 'il_mis3', ''),\
    ('Mis4', 'il_mis4', ''),\
    ('Mis5', 'il_mis5', ''),\
    ('Mis6', 'il_mis6', ''),\
    ('Mis7', 'il_mis7', ''),\
    ('Mis8', 'il_mis8', ''),\
    ('Mis9', 'il_mis9', ''),\
    ('Mis10', 'il_mis10', ''),\
    ('Fu1', 'il_fu1', ''),\
    ('Fu2', 'il_fu2', ''),\
    ('Fu3', 'il_fu3', ''),\
    ('Fu4', 'il_fu4', ''),\
    ('Fu5', 'il_fu5', ''),\
    ('Fu6', 'il_fu6', ''),\
    ('Fu7', 'il_fu7', ''),\
    ('Fu8', 'il_fu8', ''),\
    ('Fu9', 'il_fu9', ''),\
    ('Fu10', 'il_fu10', ''),\
]
# IRN_DTLS_EXT_NODE
IRN_DTLS_EXT_NODE = {\
    "BchDtls": {\
        "columnList": [\
            {"s_col": "Nm", "t_col": "il_bchdtls_nm", "dflt": ""},\
            {"s_col": "ExpDt", "t_col": "il_bchdtls_expdt", "dflt": None},\
            {"s_col": "WrDt", "t_col": "il_bchdtls_wrdt", "dflt": None},\
        ],\
    },\
}
IRN_DTLS_DFLT = [('created_by', 'il_created_by', 'System'),\
    ('updated_by', 'il_updated_by', 'System'),\
    ('is_active', 'il_is_active', 'Y'),\
    ('comments', 'il_comments', ''),\
    ('load_id', 'il_load_id', 0),\
    ('udid', 'il_udid', ''),\
    ('data_source', 'il_data_source', ''),\
    ('is_exclude', 'il_is_exclude', 'N'),\
    ('irn', 'il_irn', ''),\
]
