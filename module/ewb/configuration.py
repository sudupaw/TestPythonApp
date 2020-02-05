'''
ewb configuration details
'''
EWB_CSV_HEADER = ['User GSTIN', 'Supply Type', 'Sub Type', 'Document Type', 'Document No',\
    'Document Date', 'From_Name', 'From_GSTIN', 'Bill From_State', 'From_Address1',\
    'From_Address2', 'From_Place', 'From_Pin Code', 'From_State', 'To_Name', 'To_GSTIN',\
    'Bill To_State', 'To_Address1', 'To_Address2', 'To_Place', 'To_Pin Code', 'To_State',\
    'Line Item', 'Item code', 'Product Name', 'Description', 'HSN', 'Unit', 'Quantity',\
    'Taxable value', 'CGST Rate', 'CGST Amount', 'SGST Rate', 'SGST Amount', 'IGST Rate',\
    'IGST Amount', 'Cess Rate', 'Cess Amount', 'Trans Mode', 'Distance (Km)', 'Transporter Name',\
    'Transporter ID', 'Trans Doc No', 'Trans Doc Date', 'Vehicle No', 'Vehicle Type', 'BU',\
    'SBU', 'Location', 'User', 'Tracking Number', 'Accounting Doc No', 'Accounting Doc Date',\
    'PO No', 'PO Date', 'SO No', 'SO Date', 'Original Document No.', 'Original Document Date',\
    'MIS 1', 'MIS 2', 'MIS 3', 'MIS 4', 'MIS 5', 'MIS 6', 'MIS 7', 'MIS 8', 'MIS 9', 'MIS 10',\
    'FU 1', 'FU 2', 'FU 3', 'FU 4', 'FU 5', 'FU 6', 'FU 7', 'FU 8', 'FU 9', 'FU 10', 'FU 11',\
    'FU 12', 'FU 13', 'FU 14', 'FU 15', 'FU 16', 'FU 17', 'FU 18', 'FU 19', 'FU 20', 'FU 21',\
    'FU 22', 'FU 23', 'FU 24', 'FU 25', 'FU 26', 'FU 27', 'FU 28', 'FU 29', 'FU 30',\
    'is_ewaybill', 'irn', 'ackno', 'ackdt', 'irn_load_id', 'created_by_user']
# EWB_STRUCTURE
EWB_STRUCTURE_PAYLOAD = {"User GSTIN": "", "Supply Type": "", "Sub Type": "",\
    "Document Type": "", "Document No": "", "Document Date": "",\
    "From_Name": "", "From_GSTIN": "", "Bill From_State": "", \
    "From_Address1": "", "From_Address2": "", "From_Place" : "",\
    "From_Pin Code": "", "From_State": "", "To_Name": "",\
    "To_GSTIN": "", "Bill To_State": "", "To_Address1": "", "To_Address2": "",\
    "To_Place": "", "To_Pin Code": "", "To_State": "", "Line Item":"", "Item code": "",\
    "Product Name": "", "Description": "", "HSN": "", "Unit": "", "Quantity": "",\
    "Taxable value": "", "CGST Rate": "", "CGST Amount": "", "SGST Rate": "",\
    "SGST Amount": "", "IGST Rate": "", "IGST Amount": "", "Cess Rate":"",\
    "Cess Amount":"", "Trans Mode":"", "Distance (Km)": "", "Transporter Name": "",\
    "Transporter ID": "", "Trans Doc No": "", "Trans Doc Date": "", "Vehicle No": "",\
    "Vehicle Type": "", "BU": "", "SBU": "", "Location": "", "User": "",\
    "Tracking Number": "", "Accounting Doc No": "", "Accounting Doc Date": "", "PO No": "",\
    "PO Date": "", "SO No": "", "SO Date": "", "Original Document No.": "",\
    "Original Document Date": "", "MIS 1": "", "MIS 2":"", "MIS 3": "", "MIS 4": "",\
    "MIS 5": "", "MIS 6": "", "MIS 7": "", "MIS 8": "", "MIS 9": "", "MIS 10": "",\
    "FU 1": "", "FU 2": "", "FU 3": "", "FU 4": "", "FU 5": "", "FU 6": "", "FU 7": "",\
    "FU 8": "", "FU 9": "", "FU 10": "", "FU 11": "", "FU 12": "", "FU 13": "",\
    "FU 14": "", "FU 15": "", "FU 16": "", "FU 17": "", "FU 18": "", "FU 19": "",\
    "FU 20": "", "FU 21": "", "FU 22": "", "FU 23": "", "FU 24": "", "FU 25": "",\
    "FU 26": "", "FU 27": "", "FU 28": "", "FU 29": "", "FU 30": "", "is_ewaybill": "",\
    "irn": "", "ackno": "", "ackdt": "", "irn_load_id": "", 'created_by_user': "Irn"}
# INVOICE LEVEL DATA MAPPING
MAND_DATA_MAPPING = {
    "TranDtls": [\
        ("OutwardInward", "Supply Type", "Outward"),\
        ("SubType", "Sub Type", "Supply"),\
        ("SubTypeDescription", "FU 1", ""),\
        ("Typ", "FU 6", ""),\
    ],
    "DocDtls": [\
        ("No", "Document No", ""),\
        ("Dt", "Document Date", ""),\
        ("Typ", "Document Type", ""),\
        ("OrgInvNo", "Original Document No.", ""),\
        ("OrgInvDt", "Original Document Date", ""),\
    ],\
	"SellerDtls": [\
        ("TrdNm", "From_Name", ""),\
        ("Gstin", "From_GSTIN", ""),\
        ("Stcd", "Bill From_State", ""),\
    ],\
	"DispDtls": [\
        ("Pin", "From_Pin Code", ""),\
        ("Stcd", "From_State", ""),\
        ("Pin", "From_Pin Code", ""),\
        ("Bno", "From_Address1", ""),\
        ("Bnm", "From_Address2", ""),\
        ("Loc", "From_Place", ""),\
    ],\
	"BuyerDtls": [\
        ("TrdNm", "To_Name", ""),\
        ("Gstin", "To_GSTIN", ""),\
        ("Stcd", "Bill To_State", ""),\
    ],\
	"ShipDtls": [\
        ("Pin", "To_Pin Code", ""),\
        ("Stcd", "To_State", ""),\
        ("Pin", "To_Pin Code", ""),\
        ("Bno", "To_Address1", ""),\
        ("Bnm", "To_Address2", ""),\
        ("Loc", "To_Place", ""),\
    ],\
	"ValDtls": [\
        ("TotInvVal", "FU 4", ""),\
    ],\
	"RefDtls": [\
        ("PORef", "PO No", ""),\
        ("VendorPoRefDt", "PO Date", ""),\
        ("AccountingDocNo", "Accounting Doc No", ""),\
        ("AccountingDocDt", "Accounting Doc Date", ""),\
        ("SoNo", "SO No", ""),\
        ("SoDt", "SO Date", ""),\
    ],\
    "TransportDtls": [\
        ("TransporterId", "Transporter ID", ""),\
        ("DistanceKm", "Distance (Km)", ""),\
        ("TransporterName", "Transporter Name", ""),\
        ("TransMode", "Trans Mode", ""),\
        ("TransDocNo", "Trans Doc No", ""),\
        ("TransDocDate", "Trans Doc Date", ""),\
        ("VehicleNo", "Vehicle No", ""),\
        ("VehicleType", "Vehicle Type", ""),\
    ],\
    "MisColumns": [\
        ("Bu", "BU", ""),\
        ("Sbu", "SBU", ""),\
        ("Location", "Location", ""),\
        ("User", "User", ""),\
        ("TrackingNo", "Tracking Number", ""),\
        ("EwbNo", "FU 2", ""),\
    ]
}
# ITEM LEVEL DATA MAPPING
MAND_ITM_LVL_MAPPING = [\
    ("LineItem", "Line Item", ""),\
    ("ItemCode", "Item code", ""),\
    ("PrdNm", "Product Name", ""),\
    ("HsnCd", "HSN", ""),\
    ("Unit", "Unit", ""),\
	("Qty", "Quantity", ""),\
    ("PrdDesc", "Description", ""),\
    ("AssAmt", "Taxable value", ""),\
	("CgstRt", "CGST Rate", ""),\
    ("SgstRt", "SGST Rate", ""),\
    ("IgstRt", "IGST Rate", ""),\
	("IGST Rate", "Cess Rate", ""),\
    ("OthChrg", "FU 7", ""),\
    ("CessNonAdvolRt", "FU 8", ""),\
    ("CesNonAdVal", "FU 9", ""),\
    ("IgstAmt", "IGST Amount", ""),\
    ("CgstAmt", "CGST Amount", ""),\
    ("SgstAmt", "SGST Amount", ""),\
    ("CessAmt", "Cess Amount", ""),\
]
# UNIT TRANSFORMATION CONFIGURATION
UNIT_CONFIG = {'BAG': 'BAGS', 'BAL': 'BALE', 'BDL': 'BUNDLES', 'BKL': 'BUCKLES',\
	'BOU': 'BILLION OF UNITS', 'BOX': 'BOX', 'BTL': 'BOTTLES', 'BUN': 'BUNCHES',\
	'CAN': 'CANS', 'CBM': 'CUBIC METERS', 'CCM': 'CUBIC CENTIMETERS', 'CMS': 'CENTI METERS',\
	'CTN': 'CARTONS', 'DOZ': 'DOZENS', 'DRM': 'DRUMS', 'GGK': 'GREAT GROSS', 'GMS': 'GRAMMES',\
	'GRS': 'GROSS', 'GYD': 'GROSS YARDS', 'KGS': 'KILOGRAMS', 'KLR': 'KILOLITRE',\
	'KME': 'KILOMETRE', 'MLT': 'MILILITRE', 'MTR': 'METERS', 'MTS': 'METRIC TON',\
	'NOS': 'NUMBERS', 'OTH': 'OTHERS', 'PAC': 'PACKS', 'PCS': 'PIECES', 'PRS': 'PAIRS',\
	'QTL': 'QUINTAL', 'ROL': 'ROLLS', 'SET': 'SETS', 'SQF': 'SQUARE FEET',\
	'SQM': 'SQUARE METERS', 'SQY': 'SQUARE YARDS', 'TBS': 'TABLETS', 'TGM': 'TEN GROSS',\
	'THD': 'THOUSANDS', 'TON': 'TONNES', 'TUB': 'TUBES', 'UGS': 'US GALLONS',\
	'UNT': 'UNITS', 'YDS': 'YARDS'}
# STATE TRANSFORMATION CONFIGURATION
STATE_CONFIG = {99: 'OTHER COUNTRIES', 1: 'JAMMU AND KASHMIR', 2: 'HIMACHAL PRADESH',\
	3: 'PUNJAB', 4: 'CHANDIGARH', 5: 'UTTARAKHAND', 6: 'HARYANA', 7: 'DELHI', 8: 'RAJASTHAN',\
	9: 'UTTAR PRADESH', 10: 'BIHAR', 11: 'SIKKIM', 12: 'ARUNACHAL PRADESH', 13: 'NAGALAND',\
	14: 'MANIPUR', 15: 'MIZORAM', 16: 'TRIPURA', 17: 'MEGHALAYA', 18: 'ASSAM',\
	19: 'WEST BENGAL', 20: 'JHARKHAND', 21: 'ODISHA', 22: 'CHHATTISGARH', 23: 'MADHYA PRADESH',\
	24: 'GUJARAT', 25: 'DAMAN AND DIU', 26: 'DADRA AND NAGAR HAVELI', 27: 'MAHARASHTRA',\
	29: 'KARNATAKA', 30: 'GOA', 31: 'LAKSHADWEEP', 32: 'KERALA', 33: 'TAMIL NADU',\
	34: 'PUDUCHERRY', 35: 'ANDAMAN AND NICOBAR ISLANDS', 36: 'TELANGANA', 37: 'ANDHRA PRADESH',\
	97: 'OTHER TERRITORY'}
# STATE TRANSFORMATION LIST
STATE_TRANSFORMATION_LIST = ("Bill From_State", "From_State", "Bill To_State", "To_State")
# DOCUMENT TYPE TRANSFORMATIOn
DOC_TYPE_CONFIG = {\
    "INV": "Invoice",\
    "DBN": "Debit Note",\
    "CRN": "Credit Note",\
    "CHL": "Delivery Challan",\
    "BOE": "Bill of Entry",\
    "BIL": "Bill of supply",\
    "OTH": "Others",\
    "RCV": "Receipt Voucher",\
    "RFV": "Refund Voucher",\
    "PMV": "Payment Voucher",\
}
# Transaction type transformation config
TRAN_TYPE_CONFIG = {\
    "REG": "Address Same as Seller and Buyer (By default)",\
    "DIS": "Dispatch Address different from Seller Address",\
    "SHP": "Ship To Address is different from Buyer Address",\
    "CMB": "Both Dispatch and Shipping Address is different from Seller and Buyer respectively",\
}
# Default_value_map
DFLT_VAL_MAP = [\
    ("is_ewb", "is_ewaybill", ""),\
    ("irn", "irn", ""),\
    ("ackno", "ackno", 0),\
    ("ackdt", "ackdt", ""),\
    ("load_id", "irn_load_id", ""),\
]
