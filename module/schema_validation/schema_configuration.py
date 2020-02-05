# pylint: disable-msg=C0330
# pylint: disable-msg=C0301
# pylint: disable-msg=C0303
'''
SCHEMA validation configuration
'''
SCHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "definitions": {
    "stateCode":{
      "enum": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
        29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 97, 99],
      "minimum": 0,
      "maximum": 99,
      "type": "integer",
      "description": "statecode"
    },
    "TranDtlsSection": {
      "type": "object",
      "properties": {
        "Catg": {
          "type": "string",
          "maxLength": 3,
          "minLength": 3,
          "enum": ["B2B", "B2G", "EXP", "B2C", "b2b", "b2g", "exp", "b2c"],
          "description": "Category of Transaction: B2B-Business to Business, B2G - Business to Government, EXP - Exports "
        },
        "RegRev": {
          "type": "string",
          "maxLength": 2,
          "minLength": 2,
          "enum": ["RG", "RC", "rg", "rc"],
          "default": "RG",
          "description": "RG-Regular Charge ,RC-Reverse Charge"
        },
        "Typ": {
          "type": "string",
          "enum": ["REG", "DIS", "SHP", "CMB", "reg", "dis", "shp", "cmb"],
          "maxLength": 3,
          "minLength": 3,
          "default": "REG",
          "description": "REG-Address Same as Seller and Buyer , DIS - Dispatch Address different from Seller Address, SHP - Ship To Address is different from Buyer Address, CMB - Both Dispatch and Shipping Address is different from Seller and Buyer respectively "
        },
        "EcmTrn": {
          "type": "string",
          "maxLength": 1,
          "minLength": 1,
          "enum": ["Y", "N", "y", "n"],
          "default": "N",
          "description": " Y- Supply through E-Commerce Operator, N - Supply NOT through E-Commerce Operator"
        },
        "EcmGstin": {
          "type": "string",
          "maxLength": 15,
          "minLength": 15,
          "pattern": "[0-9]{2}[0-9|A-Z]{13}",
          "description": "GSTIN of e-Commerce operator"
        },
        "Pos": {
          "$ref": "#/definitions/stateCode"
        },
        "ClaimingRefund": {
          "type": "string",
          "maxLength": 1,
          "minLength": 1,
          "enum": ["Y", "y"],
          "description": "Whether supplier is claiming refund in case of deemed export/ SEZ supplies?"
        },
        "OutwardInward": {
          "type": "string",
          "maxLength": 7,
          "minLength": 6,
          "enum": ["OUTWARD", "INWARD", "outward", "inward"],
          "description": "Whether it is Outward or Inward supply"
        },
        "SubType": {
          "type": "string",
          "maxLength": 19,
          "minLength": 6,
          "enum": ["SUPPLY", "IMPORT", "EXPORT", "JOB WORK", "FOR OWN USE", "JOB WORK RETURNS", "SALES RETURN", "OTHERS", "SKD/CKD", "LINE SALES", "RECIPIENT NOT KNOWN", "EXHIBITION OR FAIRS", "supply", "import", "export", "job work", "for own use", "job work returns", "sales return", "others", "skd/ckd", "line sales", "recipient not known", "exhibition or fairs"],
          "description": "Sub type"
        },
        "SubTypeDescription": {
          "type": "string",
          "minLength": 0,
          "maxLength": 20,
          "description": "Sub type description"
        },
        "DiffPercentage": {
          "type": "string",
          "maxLength": 4,
          "minLength": 4,
          "enum": ["0.65"],
          "description": "Differential percentage -  For capturing exemption provided to leased car transaction. In case exemption is applicable, capture 0.65"
        },
        "Taxability": {
          "maxLength": 15,
          "minLength": 6,
          "enum": ["TAXABLE", "NIL RATED", "EXEMPTED", "NON GST", "EXPORT", "DEEMED EXPORT", "SUPPLY TO SEZ", "NO SUPPLY", "SUPPLY FROM SEZ", "IMPORT", "taxable", "nil rated", "exempted", "non gst", "export", "deemed export", "supply to sez", "no supply", "supply from sez", "import"],
          "description": "Taxability of transaction"
        },
        "InterIntra": {
          "type": "string",
          "maxLength": 5,
          "minLength": 5,
          "enum": ["INTER", "INTRA", "inter", "intra"],
          "description": "Inter state'or 'Intra state"
        }
      },
      "required": ["Catg", "RegRev", "Typ"]
    },
    "DocDtlsSection": {
      "type": "object",
      "properties": {
        "Typ": {
          "type": "string",
          "maxLength": 3,
          "enum": ["INV", "CRN", "DBN", "BIL", "BOE", "CHL", "OTH", "RCV", "RFV", "PMV", "inv", "crn", "dbn", "bil", "boe", "chl", "oth", "rcv", "rfv", "pmv"],
          "description": "Document Type: INV-INVOICE, CRN-CREDIT NOTE, DBN-DEBIT NOTE"
        },
        "No": {
          "type": "string",
          "maxLength": 16,
          "minLength": 1,
          "pattern": "[0-9|A-Z|a-z|/|-]{1,16}",
          "description": "Document Number"
        },
        "Dt": {
          "type": "string",
          "maxLength": 10,
          "minLength": 10,
          "pattern": "[2][0][1-2][0-9]-[0-1][0-9]-[0-3][0-9]",
          "description": "Document Date"
        },
        "OrgInvNo": {
          "type": "string",
          "maxLength": 16,
          "minLength": 0,
          "pattern": "[0-9|A-Z|a-z|/|-|(|)]{0,16}",
          "description": "Original Invoice Number in case of Credit / Debit note"
        },
        "OrgInvDt": {
          "type": "string",
          "maxLength": 10,
          "minLength": 10,
          "pattern": "[2][0][1-2][0-9]-[0-1][0-9]-[0-3][0-9]",
          "description": "Original Invoice Date in case of Credit / Debit Note"
        },
        "ReasonForCnDn": {
          "type": "string",
          "maxLength": 250,
          "minLength": 0,
          "description": "Reason for issuance of CN/DN"
        }
      },
      "required": ["Typ", "No", "Dt"]
    },
    "SellerDtlsSection": {
      "type": "object",
      "properties": {
        "Gstin": {
          "type": "string",
          "maxLength": 15,
          "minLength": 3,
          "pattern": "[0-9]{2}[0-9|A-Z]{13}|URP",
          "description": "GSTIN"
        },
        "TrdNm": {
          "type": "string",
          "minLength": 3,
          "maxLength": 100,
          "description": "Tradename"
        },
        "Bno": {
          "type": "string",
          "minLength": 0,
          "maxLength": 60,
          "description": "Building no."
        },
        "Bnm": {
          "type": "string",
          "minLength": 0,
          "maxLength": 60,
          "description": "Building name"
        },
        "Flno": {
          "type": "string",
          "minLength": 0,
          "maxLength": 60,
          "description": "Floor no."
        },
        "Loc": {
          "type": "string",
          "minLength": 3,
          "maxLength": 60,
          "description": "Location"
        },
        "Dst": {
          "type": "string",
          "minLength": 0,
          "maxLength": 60,
          "description": "District"
        },
        "Pin": {
          "type": "integer",
          "maximum": 999999,
          "minimum": 100000,
          "description": "Pincode"
        },
        "Stcd": {
          "$ref": "#/definitions/stateCode"
        },
        "Ph": {
          "type": "integer",
          "minimum": 1000000000,
          "maximum": 9999999999,
          "description": "Phone or Mobile No."
        },
        "Em": {
          "type": "string",
          "maxLength": 50,
          "minLength": 10,
          "description": "Email-Id"
        },
        "SupplierCode": {
          "type": "string",
          "maxLength": 250,
          "minLength": 0,
          "description": "Supplier code as per books in case of inward transaction"
        }
      },
      "required": ["Gstin", "TrdNm", "Loc", "Pin", "Stcd"]
    },
    "BuyerDtlsSection": {
      "type": "object",
      "properties": {
        "Gstin": {
          "type": "string",
          "maxLength": 15,
          "minLength": 3,
          "pattern": "(^[0-9]{2}[0-9|A-Z]{13}$)|URP",
          "description": "GSTIN"
        },
        "TrdNm": {
          "type": "string",
          "minLength": 3,
          "maxLength": 100,
          "description": "Tradename"
        },
        "Bno": {
          "type": "string",
          "minLength": 0,
          "maxLength": 60,
          "description": "Building no."
        },
        "Bnm": {
          "type": "string",
          "minLength": 0,
          "maxLength": 60,
          "description": "Building name"
        },
        "Flno": {
          "type": "string",
          "minLength": 0,
          "maxLength": 60,
          "description": "Floor no."
        },
        "Loc": {
          "type": "string",
          "minLength": 3,
          "maxLength": 60,
          "description": "Location"
        },
        "Dst": {
          "type": "string",
          "minLength": 0,
          "maxLength": 60,
          "description": "District"
        },
        "Pin": {
          "type": "integer",
          "maximum": 999999,
          "minimum": 100000,
          "description": "Pincode"
        },
        "Stcd": {
          "$ref": "#/definitions/stateCode"
        },
        "Ph": {
          "type": "integer",
          "minimum": 1000000000,
          "maximum": 9999999999,
          "description": "Phone or Mobile No."
        },
        "Em": {
          "type": "string",
          "maxLength": 50,
          "minLength": 10,
          "description": "Email-Id"
        },
        "CustomerCode": {
          "type": "string",
          "maxLength": 250,
          "minLength": 0,
          "description": "Supplier code as per books in case of inward transaction"
        }
      },
      "required": ["Gstin", "TrdNm", "Loc", "Pin", "Stcd"]
    },
    "DispDtlsSection": {
      "type": "object",
      "properties": {
        "Gstin": {
          "type": "string",
          "maxLength": 15,
          "minLength": 3,
          "pattern": "[0-9]{2}[0-9|A-Z]{13}|URP",
          "description": "GSTIN"
        },
        "TrdNm": {
          "type": "string",
          "minLength": 5,
          "maxLength": 100,
          "description": "Name of the Person or Tradename"
        },
        "Bno": {
          "type": "string",
          "maxLength": 60,
          "description": "Building no."
        },
        "Bnm": {
          "type": "string",
          "maxLength": 60,
          "description": "Building name"
        },
        "Flno": {
          "type": "string",
          "maxLength": 60,
          "description": "Floor no."
        },
        "Loc": {
          "type": "string",
          "minLength": 3,
          "maxLength": 60,
          "description": "Location"
        },
        "Dst": {
          "type": "string",
          "maxLength": 60,
          "description": "District"
        },
        "Pin": {
          "type": "integer",
          "maximum": 999999,
          "minimum": 100000,
          "description": "Pincode"
        },
        "Stcd": {
          "$ref": "#/definitions/stateCode"
        },
        "Ph": {
          "type": "integer",
          "minimum": 1000000000,
          "maximum": 9999999999,
          "description": "Phone or Mobile No."
        },
        "Em": {
          "type": "string",
          "maxLength": 50,
          "minLength": 10,
          "description": "Email-Id"
        }
      },
      "required": ["Gstin", "TrdNm", "Loc", "Pin", "Stcd"]
    },
    "ShipDtlsSection": {
      "type": "object",
      "properties": {
        "Gstin": {
          "type": "string",
          "maxLength": 15,
          "minLength": 3,
          "pattern": "[0-9]{2}[0-9|A-Z]{13}|URP",
          "description": "GSTIN"
        },
        "TrdNm": {
          "type": "string",
          "minLength": 5,
          "maxLength": 100,
          "description": "Name of the person or Tradename"
        },
        "Bno": {
          "type": "string",
          "minLength": 0,
          "maxLength": 60,
          "description": "Building no."
        },
        "Bnm": {
          "type": "string",
          "minLength": 0,
          "maxLength": 60,
          "description": "Building name."
        },
        "Flno": {
          "type": "string",
          "minLength": 0,
          "maxLength": 60,
          "description": "Floor no."
        },
        "Loc": {
          "type": "string",
          "minLength": 3,
          "maxLength": 60,
          "description": "Location."
        },
        "Dst": {
          "type": "string",
          "minLength": 0,
          "maxLength": 60,
          "description": "District"
        },
        "Pin": {
          "type": "integer",
          "maximum": 999999,
          "minimum": 100000,
          "description": "Pincode"
        },
        "Stcd": {
          "$ref": "#/definitions/stateCode"
        },
        "Ph": {
          "type": "integer",
          "minimum": 1000000000,
          "maximum": 9999999999,
          "description": "Phone or Mobile No."
        },
        "Em": {
          "type": "string",
          "maxLength": 50,
          "minLength": 10,
          "description": "Email-Id"
        }
      },
      "required": ["Gstin", "TrdNm", "Loc", "Pin", "Stcd"]
    },
    "UQCEnum": {
      "enum": ["BAG", "BAL", "BDL", "BKL", "BOU", "BOX", "BTL", "BUN", "CAN", "CBM", "CCM", "CMS", "CTN", "DOZ", "DRM", "GGK", "GMS", "GRS", "GYD", "KGS", "KLR", "KME", "MLT", "MTR", "MTS", "NOS", "PAC", "PCS", "PRS", "QTL", "ROL", "SET", "SQF", "SQM", "SQY", "TBS", "TGM", "THD", "TON", "TUB", "UGS", "UNT", "LTR", "YDS", "bag", "bal", "bdl", "bkl", "bou", "box", "btl", "bun", "can", "cbm", "ccm", "cms", "ctn", "doz", "drm", "ggk", "gms", "grs", "gyd", "kgs", "klr", "kme", "mlt", "mtr", "mts", "nos", "pac", "pcs", "prs", "qtl", "rol", "set", "sqf", "sqm", "sqy", "tbs", "tgm", "thd", "ton", "tub", "ugs", "unt", "ltr", "yds"],
      "maxLength": 8,
      "type": "string",
      "description": "Unit"
    },
    "two50Length": {
      "type": "string",
      "maxLength": 250,
      "minLength": 0
    },
    "taxableValue": {
      "type": "number",
      "minimum": 0,
      "maximum": 99999999999999.99,
      "maxLength": 17
    },
    "InvoiceItemDetails": {
      "properties": {
        "LineItem": {
          "type": "integer",
          "minimum": 0,
          "maximum": 99999,
          "description": "Line item number of document"
        },
        "ItemCode": {
          "$ref": "#/definitions/two50Length",
          "description": "Item code as per books"
        },
        "PrdNm": {
          "type": "string",
          "minLength": 3,
          "maxLength": 100,
          "description": "Product Name"
        },
        "PrdDesc": {
          "type": "string",
          "minLength": 0,
          "maxLength": 100,
          "description": "Product Description"
        },
        "HsnCd": {
          "type": "string",
          "minLength": 4,
          "maxLength": 8,
          "description": "HSN Code"
        },
        "GoodsService": {
          "type": "string",
          "maxLength": 1,
          "minLength": 1,
          "enum": ["G", "S", "g", "s"],
          "description": "Goods or Service"
        },
        "Barcde": {
          "type": "string",
          "minLength": 0,
          "maxLength": 30,
          "description": "Bar Code"
        },
        "Qty": {
          "type": "number",
          "minimum": 0,
          "maximum": 999999999.99,
          "multipleOf": 0.01,
          "maxLength": 12,
          "description": "Quantity"
        },
        "FreeQty": {
          "type": "number",
          "minimum": 0,
          "maximum": 999999999.99,
          "multipleOf": 0.01,
          "maxLength": 12,
          "description": "Free Quantity"
        },
        "Unit": {
          "$ref": "#/definitions/UQCEnum"
        },
        "UnitPrice": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "maxLength": 17,
          "description": "Unit Price"
        },
        "TotAmt": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "maxLength": 17,
          "description": "Total Amount (Unit Price * Quantity)"
        },
        "Discount": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "maxLength": 17,
          "description": "Discount"
        },
        "OthChrg": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "maxLength": 17,
          "description": "Other Charges"
        },
        "AssAmt": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "maxLength": 17,
          "description": "Assessable Amount (Total Amount -Discount + Other charges)"
        },
        "CgstRt": {
          "type": "number",
          "maximum": 999.999,
          "minimum": 0,
          "enum": [0, 0.05, 0.125, 0.5, 0.75, 1.5, 2.5, 3.75, 6, 9, 14],
          "description": "CGSTRate"
        },
        "SgstRt": {
          "type": "number",
          "maximum": 999.999,
          "minimum": 0,
          "enum": [0, 0.05, 0.125, 0.5, 0.75, 1.5, 2.5, 3.75, 6, 9, 14],
          "description": "SGSTRate"
        },
        "IgstRt": {
          "type": "number",
          "maximum": 999.999,
          "minimum": 0,
          "enum": [0, 0.1, 0.25, 1, 1.5, 3, 5, 7.5, 12, 18, 28],
          "description": "IGSTRate"
        },
        "CesRt": {
          "type": "number",
          "maximum": 999.999,
          "multipleOf": 0.001,
          "description": "CESSRate",
          "minimum": 0
        },
        "CesNonAdVal": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "maxLength": 17,
          "description": "Cess Non-Advol Amount"
        },
        "StateCes": {
          "type": "number",
          "maximum": 999.999,
          "multipleOf": 0.001,
          "description": "State CESS Rate",
          "minimum": 0
        },
        "TotItemVal": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "maxLength": 17,
          "description": "Total Item Value : Assessable Amount [1 + (CGST Rate + SGST Rate + Cess Rate + State Cess Rate)] + Cess NonAdvol Amount "
        },
        "BchDtls": {
          "type": "object",
          "properties": {
            "Nm": {
              "type": "string",
              "minLength": 0,
              "maxLength": 20,
              "description": "Batch name"
            },
            "ExpDt": {
              "type": "string",
              "maxLength": 10,
              "minLength": 10,
              "pattern": "[2][0][1-2][0-9]-[0-1][0-9]-[0-3][0-9]",
              "description": "Batch Expiry Date"
            },
            "WrDt": {
              "type": "string",
              "maxLength": 10,
              "minLength": 10,
              "pattern": "[2][0][1-2][0-9]-[0-1][0-9]-[0-3][0-9]",
              "description": "Warranty Date"
            }
          }
        },
        "Vat": {
          "$ref": "#/definitions/taxableValue",
          "description": "VAT"
        },
        "CentralExcise": {
          "$ref": "#/definitions/taxableValue",
          "description": "Central Excise"
        },
        "StateExcise": {
          "$ref": "#/definitions/taxableValue",
          "description": "State Excise"
        },
        "ExportDuty": {
          "$ref": "#/definitions/taxableValue",
          "description": "Export Duty (In case of exports)"
        },
        "ValueBeforeBcd": {
          "$ref": "#/definitions/taxableValue",
          "description": "Assessable value before BCD (In case of imports)"
        },
        "Bcd": {
          "$ref": "#/definitions/taxableValue",
          "description": "Basic Custom Duty (In case of imports)"
        },
        "TotalGstRate": {
          "type": "number",
          "minimum": 0,
          "maximum": 999.999,
          "description": "Total_GST_Rate"
        },
        "CessNonAdvolRt": {
          "$ref": "#/definitions/taxableValue",
          "description": "Cess Non Advol Rate"
        },
        "IgstAmt": {
          "$ref": "#/definitions/taxableValue",
          "description": "IGST Amount as per item"
        },
        "CgstAmt": {
          "$ref": "#/definitions/taxableValue",
          "description": "CGST Amount as per item"
        },
        "SgstAmt": {
          "$ref": "#/definitions/taxableValue",
          "description": "SGST Amount as per item"
        },
        "CessAmt": {
          "$ref": "#/definitions/taxableValue",
          "description": "CESS Amount as per item"
        },
        "EligibilityItc": {
          "type": "string",
          "maxLength": 2,
          "minLength": 2,
          "enum": ["IP", "CP", "IS", "NO", "ip", "cp", "is", "no"],
          "description": "Eligibility of ITC IP-Input, CP-Capital, IS-Input Service, No-No"
        },
        "ItcIgst": {
          "$ref": "#/definitions/taxableValue",
          "description": "ITC_IGST"
        },
        "ItcCgst": {
          "$ref": "#/definitions/taxableValue",
          "description": "ITC_CGST"
        },
        "ItcSgst": {
          "$ref": "#/definitions/taxableValue",
          "description": "ITC_SGST"
        },
        "ItcCess": {
          "$ref": "#/definitions/taxableValue",
          "description": "ITC_Cess"
        },
        "NatureOfExpense": {
          "type": "string",
          "maxLength": 250,
          "enum": ["EXCLUSIVELY FOR NON- BUSINESS PURPOSES", "EXCLUSIVELY FOR EXEMPTED SUPPLIES", "INELIGIBLE PROCUREMENTS U/S 17(5)",
            "EXCLUSIVELY FOR TAXABLE/ ZERO-RATED SUPPLIES", "COMMON FOR BUSINESS & NON-BUSINESS PURPOSES", "COMMON FOR TAXABLE & EXEMPTED SUPPLIES",
            "exclusively for non- business purposes", "exclusively for exempted supplies", "ineligible procurements u/s 17(5)",
            "exclusively for taxable/ zero-rated supplies", "common for business & non-business purposes", "common for taxable & exempted supplies"],
          "description": "Nature of expense"
        },
        "Mis1": {
          "$ref": "#/definitions/two50Length",
          "description": "Fields for MIS purposes at item level"
        },
        "Mis2": {
          "$ref": "#/definitions/two50Length",
          "description": "Fields for MIS purposes at item level"
        },
        "Mis3": {
          "$ref": "#/definitions/two50Length",
          "description": "Fields for MIS purposes at item level"
        },
        "Mis4": {
          "$ref": "#/definitions/two50Length",
          "description": "Fields for MIS purposes at item level"
        },
        "Mis5": {
          "$ref": "#/definitions/two50Length",
          "description": "Fields for MIS purposes at item level"
        },
        "Mis6": {
          "$ref": "#/definitions/two50Length",
          "description": "Fields for MIS purposes at item level"
        },
        "Mis7": {
          "$ref": "#/definitions/two50Length",
          "description": "Fields for MIS purposes at item level"
        },
        "Mis8": {
          "$ref": "#/definitions/two50Length",
          "description": "Fields for MIS purposes at item level"
        },
        "Mis9": {
          "$ref": "#/definitions/two50Length",
          "description": "Fields for MIS purposes at item level"
        },
        "Mis10": {
          "$ref": "#/definitions/two50Length",
          "description": "Fields for MIS purposes at item level"
        },
        "Fu1": {
          "$ref": "#/definitions/two50Length",
          "description": "Fields for future use at item level"
        },
        "Fu2": {
          "$ref": "#/definitions/two50Length",
          "description": "Fields for future use at item level"
        },
        "Fu3": {
          "$ref": "#/definitions/two50Length",
          "description": "Fields for future use at item level"
        },
        "Fu4": {
          "$ref": "#/definitions/two50Length",
          "description": "Fields for future use at item level"
        },
        "Fu5": { 
          "$ref": "#/definitions/two50Length",
          "description": "Fields for future use at item level"
        },
        "Fu6": {
          "$ref": "#/definitions/two50Length",
          "description": "Fields for future use at item level"
        },
        "Fu7": {
          "$ref": "#/definitions/two50Length",
          "description": "Fields for future use at item level"
        },
        "Fu8": {
          "$ref": "#/definitions/two50Length",
          "description": "Fields for future use at item level"
        },
        "Fu9": {
          "$ref": "#/definitions/two50Length",
          "description": "Fields for future use at item level"
        },
        "Fu10": {
          "$ref": "#/definitions/two50Length",
          "description": "Fields for future use at item level"
        }
      },
      "required": ["PrdNm", "HsnCd", "Qty", "Unit", "CgstRt", "SgstRt",
        "IgstRt", "CesRt", "CesNonAdVal", "StateCes", "TotItemVal"],
      "type": "object"
    },
    "ValDtlsSection": {
      "type": "object",
      "properties": {
        "AssVal": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "maxLength": 17,
          "description": "Total Assessable value of all items"
        },
        "CgstVal": {
          "type": "number",
          "maxLength": 17,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "minimum": 0,
          "description": "Total CGST value of all items"
        },
        "SgstVal": {
          "type": "number",
          "minimum": 0,
          "maxLength": 17,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "description": "Total SGST value of all items"
        },
        "IgstVal": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "maxLength": 17,
          "description": "Total IGST value of all items"
        },
        "CesVal": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "maxLength": 17,
          "description": "Total CESS value of all items"
        },
        "StCesVal": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "maxLength": 17,
          "description": "Total State CESS value of all items"
        },
        "CesNonAdVal": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "maxLength": 17,
          "description": "Total Cess Non-advol value of all items"
        },
        "Disc": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "maxLength": 17,
          "description": "Discount on invoice value if any"
        },
        "OthChrg": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "maxLength": 17,
          "description": "Other charges if any"
        },
        "TotInvVal": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "maxLength": 17,
          "description": "Final Invoice value "
        }
      },
      "required": ["AssVal", "CgstVal", "SgstVal", "IgstVal", "CesVal", "StCesVal",
        "CesNonAdVal", "TotInvVal"]
    },
    "PayDtlsSection": {
      "type": "object",
      "properties": {
        "Nam": {
          "type": "string",
          "maxLength": 100,
          "description": "Payee Name"
        },
        "Mode": {
          "type": "string",
          "maxLength": 6,
          "enum": ["CASH", "EPAY", "DIRDBT", "OTH", "cash", "epay", "dirdbt", "oth"],
          "description": "Mode of Payment"
        },
        "FinInsBr": {
          "type": "string",
          "maxLength": 11,
          "description": "Branch or IFSC code"
        },
        "PayTerm": {
          "type": "string",
          "maxLength": 200,
          "description": "Terms of Payment"
        },
        "PayInstr": {
          "type": "string",
          "maxLength": 200,
          "description": "Payment Instruction"
        },
        "CrTrn": {
          "type": "string",
          "maxLength": 50,
          "description": "Credit Transfer"
        },
        "DirDr": {
          "type": "string",
          "maxLength": 50,
          "description": "Direct Debit"
        },
        "CrDay": {
          "type": "number",
          "minimum": 0,
          "maxLength": 3,
          "maximum": 999,
          "description": "Credit Days"
        },
        "BalAmt": {
          "type": "number",
          "minimum": 0,
          "maxLength": 17,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "description": "Balance Amount to be paid"
        },
        "PayDueDt": {
          "type": "string",
          "maxLength": 10,
          "inLength": 10,
          "pattern": "[2][0][1-2][0-9]-[0-1][0-9]-[0-3][0-9]",
          "description": "Due Date of Payment"
        },
        "AcctDet": {
          "type": "string",
          "maxLength": 50,
          "minLength": 0,
          "description": "Account Details"
        }
      }
    },
    "RefDtlsSection": {
      "type": "object",
      "properties": {
        "InvRmk": {
          "type": "string",
          "maxLength": 100,
          "minLength": 0,
          "pattern": "[0-9|A-Z|a-z|/|-|(|)]{0,100}",
          "description": "Invoice Remarks"
        },
        "InvStDt": {
          "type": "string",
          "maxLength": 10,
          "minLength": 10,
          "pattern": "[2][0][1-2][0-9]-[0-1][0-9]-[0-3][0-9]",
          "description": "Invoice Period Start Date"
        },
        "InvEndDt": {
          "type": "string",
          "maxLength": 10,
          "minLength": 10,
          "pattern": "[2][0][1-2][0-9]-[0-1][0-9]-[0-3][0-9]",
          "description": "Invoice Period End Date"
        },
        "PrecInvNo": {
          "type": "string",
          "maxLength": 20,
          "minLength": 1,
          "pattern": "[0-9|A-Z|a-z|/|-]{1,20}",
          "description": "Preceeding Invoice Number"
        },
        "PrecInvDt": {
          "type": "string",
          "maxLength": 10,
          "minLength": 10,
          "pattern": "[2][0][1-2][0-9]-[0-1][0-9]-[0-3][0-9]",
          "description": "Preceding Invoice Date"
        },
        "RecAdvRef": {
          "type": "string",
          "maxLength": 20,
          "minLength": 1,
          "pattern": "[0-9|A-Z|a-z|/|-|(|)]{1,20}",
          "description": "Receipt Advice No."
        },
        "TendRef": {
          "type": "string",
          "maxLength": 20,
          "minLength": 1,
          "pattern": "[0-9|A-Z|a-z|/|-|(|)]{1,20}",
          "description": "Lot/Batch Reference No."
        },
        "ContrRef": {
          "type": "string",
          "maxLength": 20,
          "minLength": 1,
          "pattern": "[0-9|A-Z|a-z|/|-|(|)]{1,20}",
          "description": "Contract Reference Number"
        },
        "ExtRef": {
          "type": "string",
          "maxLength": 20,
          "minLength": 1,
          "pattern": "[0-9|A-Z|a-z|/|-|(|)]{1,20}",
          "description": "Any other reference"
        },
        "ProjRef": {
          "type": "string",
          "maxLength": 20,
          "minLength": 1,
          "pattern": "[0-9|A-Z|a-z|/|-|(|)]{1,20}",
          "description": "Project Reference Number"
        },
        "PORef": {
          "type": "string",
          "maxLength": 20,
          "minLength": 1,
          "pattern": "[0-9|A-Z|a-z|/|-|(|)]{1,20}",
          "description": "Vendor PO Reference Number"
        },
        "VendorPoRefDt": {
          "type": "string",
          "maxLength": 10,
          "minLength": 10,
          "pattern": "[2][0][1-2][0-9]-[0-1][0-9]-[0-3][0-9]",
          "description": "Vendor PO Reference date"
        },
        "AccountingDocNo": {
          "type": "string",
          "maxLength": 250,
          "minLength": 0,
          "description": "Accounting document No"
        },
        "AccountingDocDt": {
          "type": "string",
          "maxLength": 10,
          "minLength": 10,
          "pattern": "[2][0][1-2][0-9]-[0-1][0-9]-[0-3][0-9]",
          "description": "Accounting document Date"
        },
        "SoNo": {
          "type": "string",
          "maxLength": 250,
          "minLength": 0,
          "description": "Sales order number"
        },
        "SoDt": {
          "type": "string",
          "maxLength": 10,
          "minLength": 10,
          "pattern": "[2][0][1-2][0-9]-[0-1][0-9]-[0-3][0-9]",
          "description": "Sales order date"
        }
      }
    },
    "portList":{
      "type": "string",
      "maxLength": 6,
      "minLength": 6,
      "enum": ["INABG1", "INACH1", "INADA6", "INADI1", "INAGI1", "INAGR4", "INAGR5", "INAGR6", "INAGTB", "INAGX4", "INAHD6", "INAIG6", "INAII6", "INAIK6", "INAIR6", "INAJE6", "INAJJ6", "INAJL4", "INAJM6", "INAKB6", "INAKD4", "INAKP6", "INAKR6", "INAKV6", "INALA1", "INALF1", "INAMD4", "INAMD5", "INAMD6", "INAMG6", "INAMI1", "INAMK6", "INANG1", "INANL1", "INAPI6", "INAPL6", "INAPT6", "INARR6", "INASR2", "INASR6", "INATQ4", "INATQ6", "INATRB", "INATT2", "INAWM6", "INAWS6", "INAWW6", "INAZK1", "INBAG6", "INBAI6", "INBAM6", "INBAP6", "INBAT6", "INBAU6", "INBAW6", "INBBI4", "INBBM6", "INBBP1", "INBBS6", "INBCH6", "INBCO6", "INBCP6", "INBDB6", "INBDG1", "INBDH6", "INBDI6", "INBDM6", "INBDQ1", "INBDR1", "INBED1", "INBEK4", "INBEP4", "INBET1", "INBEY1", "INBFR6", "INBGK6", "INBGMB", "INBGQ6", "INBGUB", "INBGW1", "INBHC6", "INBHD6", "INBHJ4", "INBHL6", "INBHM1", "INBHO4", "INBHS6", "INBHU1", "INBHU4", "INBKB4", "INBKR1", "INBKT1", "INBLC6", "INBLE6", "INBLJ6", "INBLK1", "INBLM1", "INBLP1", "INBLR4", "INBLR5", "INBLR6", "INBLTB", "INBLV6", "INBMA6", "INBMR2", "INBNC6", "INBND1", "INBNG6", "INBNK6", "INBNP1", "INBNRB", "INBNT6", "INBNW6", "INBNX6", "INBNYB", "INBOK6", "INBOLB", "INBOM1", "INBOM4", "INBOM5", "INBOM6", "INBPL5", "INBPS5", "INBRAB", "INBRC6", "INBRH1", "INBRI6", "INBRL6", "INBRM1", "INBRS6", "INBRY1", "INBSAB", "INBSB6", "INBSL6", "INBSN1", "INBSR1", "INBSW6", "INBTK1", "INBTMB", "INBTR1", "INBUD1", "INBUL6", "INBUP4", "INBUP6", "INBVC6", "INBWD6", "INBWN1", "INBXR6", "INBYT1", "INCAG6", "INCAM1", "INCAP1", "INCAR1", "INCAS6", "INCBC6", "INCBD4", "INCBDB", "INCBE6", "INCBL1", "INCBS6", "INCCH6", "INCCI6", "INCCJ1", "INCCJ4", "INCCP6", "INCCQ6", "INCCT6", "INCCU1", "INCCU4", "INCCU5", "INCCW6", "INCDC6", "INCDD6", "INCDL1", "INCDP1", "INCDP4", "INCDP6", "INCDQ6", "INCDR6", "INCEC6", "INCGA6", "INCGE6", "INCGI6", "INCGL6", "INCHE6", "INCHJ6", "INCHL1", "INCHMB", "INCHN6", "INCHPB", "INCHR1", "INCJA6", "INCJB4", "INCJB6", "INCJC6", "INCJD6", "INCJE6", "INCJF6", "INCJH6", "INCJI6", "INCJJ6", "INCJN6", "INCJO6", "INCJS6", "INCLK6", "INCLU6", "INCLX6", "INCMB1", "INCML6", "INCNB1", "INCNC6", "INCNN1", "INCOA6", "INCOH4", "INCOK1", "INCOK4", "INCOK6", "INCOL1", "INCOO1", "INCOP6", "INCPC6", "INCPL6", "INCPR6", "INCRL6", "INCRN1", "INCRW6", "INCRXB", "INCSP6", "INCSV6", "INCTI1", "INCUM1", "INDAE4", "INDAH1", "INDAI4", "INDAM1", "INDAM4", "INDAR6", "INDBD4", "INDBS6", "INDDL6", "INDEA6", "INDED4", "INDEF6", "INDEG1", "INDEH6", "INDEI6", "INDEJ6", "INDEL4", "INDEL5", "INDEM6", "INDEN6", "INDEP4", "INDER6", "INDES6", "INDET6", "INDEU6", "INDEW6", "INDGI6", "INDGT6", "INDHA6", "INDHBB", "INDHLB", "INDHM4", "INDHN1", "INDHP1", "INDHR1", "INDHU1", "INDIB4", "INDID6", "INDIG1", "INDIG6", "INDIT6", "INDIU1", "INDIU4", "INDIV1", "INDLAB", "INDLH6", "INDLI2", "INDLOB", "INDLUB", "INDMA1", "INDMRB", "INDMT1", "INDMU4", "INDPC4", "INDPR6", "INDRC6", "INDRGB", "INDRK1", "INDRL1", "INDRU6", "INDSK1", "INDSM6", "INDTW1", "INDUR6", "INDWA1", "INDWKB", "INDWN6", "INDWR6", "INENR1", "INERP6", "INERV6", "INESH1", "INFBD6", "INFBE6", "INFBM6", "INFBP6", "INFBRB", "INFBS6", "INFCH5", "INFLT6", "INFMA6", "INFMH6", "INFMJ6", "INFMS6", "INGAIB", "INGALB", "INGAO6", "INGAS6", "INGAU1", "INGAU2", "INGAU4", "INGAU5", "INGAW2", "INGAY4", "INGDL6", "INGDM6", "INGDP6", "INGED2", "INGGA1", "INGGB6", "INGGC6", "INGGD6", "INGGE6", "INGGF6", "INGGG6", "INGGI6", "INGGL6", "INGGM6", "INGGN2", "INGGO6", "INGGP6", "INGGS6", "INGGU6", "INGGV1", "INGHA1", "INGHC6", "INGHPB", "INGHR6", "INGHWB", "INGID6", "INGIN6", "INGJIB", "INGJXB", "INGKJ2", "INGKJB", "INGLY6", "INGMI6", "INGNA6", "INGNC6", "INGNG6", "INGNL6", "INGNP6", "INGNR6", "INGNT6", "INGOI4", "INGOP4", "INGPB6", "INGPR1", "INGRD6", "INGRL6", "INGRN6", "INGRR6", "INGRS6", "INGRW6", "INGTGB", "INGTI6", "INGTR2", "INGTS6", "INGTZB", "INGUX4", "INGWL4", "INGWL6", "INGWM4", "INHAL1", "INHAN6", "INHAO6", "INHAS6", "INHBB6", "INHBX4", "INHDD6", "INHEB6", "INHEI6", "INHEM6", "INHGLB", "INHGT1", "INHIR6", "INHJR4", "INHLD2", "INHLE6", "INHLIB", "INHND1", "INHON1", "INHPI6", "INHRN1", "INHSF6", "INHSP6", "INHSS4", "INHST6", "INHSU6", "INHTSB", "INHUR6", "INHWR1", "INHYB6", "INHYD4", "INHYD5", "INHYD6", "INHZA1", "INHZA6", "INIDR4", "INIDR6", "INIGU6", "INILP6", "INIMF4", "ININB6", "ININD6", "ININI6", "ININN6", "ININT6", "INISK4", "INISK6", "INIXA4", "INIXB4", "INIXC4", "INIXD4", "INIXE1", "INIXE4", "INIXG4", "INIXH4", "INIXI4", "INIXJ4", "INIXK4", "INIXL4", "INIXL5", "INIXM4", "INIXM6", "INIXN4", "INIXP4", "INIXQ4", "INIXR4", "INIXS4", "INIXT4", "INIXU4", "INIXW4", "INIXW6", "INIXY1", "INIXY4", "INIXY6", "INIXZ1", "INIXZ4", "INJAI4", "INJAI5", "INJAI6", "INJAK1", "INJAL6", "INJAYB", "INJBD1", "INJBL6", "INJBNB", "INJDA1", "INJDH4", "INJDH6", "INJGA4", "INJGB4", "INJGD1", "INJGI6", "INJHA6", "INJHOB", "INJHV6", "INJIGB", "INJJK6", "INJKA6", "INJLR4", "INJNJ6", "INJNR4", "INJNR6", "INJPGB", "INJPI6", "INJPV6", "INJPW6", "INJRH4", "INJSA4", "INJSG6", "INJSM6", "INJSZ6", "INJTP1", "INJUC6", "INJUX6", "INJWAB", "INKAK1", "INKAK6", "INKAL1", "INKAP6", "INKAR6", "INKAT1", "INKBC6", "INKBT1", "INKCG6", "INKDD6", "INKDI1", "INKDL6", "INKDN1", "INKDP1", "INKELB", "INKGG6", "INKGJ1", "INKHD6", "INKIW1", "INKJA6", "INKJB6", "INKJD6", "INKJG6", "INKJH6", "INKJIB", "INKJM6", "INKJR6", "INKKR1", "INKKU6", "INKLB6", "INKLC6", "INKLG6", "INKLH4", "INKLI6", "INKLK6", "INKLM6", "INKLN6", "INKLS6", "INKLY1", "INKMAB", "INKMB1", "INKMI6", "INKML6", "INKND1", "INKNK6", "INKNLB", "INKNU4", "INKNU5", "INKNU6", "INKOC5", "INKOD1", "INKOI1", "INKOK1", "INKON1", "INKPK6", "INKRI1", "INKRK1", "INKRM6", "INKRN1", "INKRP1", "INKRW1", "INKSG1", "INKSH1", "INKSP1", "INKTD1", "INKTGB", "INKTI1", "INKTRB", "INKTT6", "INKTU4", "INKTU6", "INKTW1", "INKTY6", "INKUK1", "INKUK6", "INKUR6", "INKUU4", "INKVI1", "INKVL1", "INKVR6", "INKVT1", "INKWAB", "INKWGB", "INKWHB", "INKXJ2", "INKYM6", "INKZE6", "INKZP6", "INKZT6", "INLCH6", "INLDA4", "INLDH6", "INLGLB", "INLKO4", "INLKQB", "INLON6", "INLPB6", "INLPC6", "INLPD6", "INLPG6", "INLPI6", "INLPJ6", "INLPM6", "INLPR1", "INLPS6", "INLPW6", "INLTBB", "INLUD6", "INLUH4", "INLUH5", "INLUH6", "INLWG6", "INMAA1", "INMAA4", "INMAA5", "INMAA6", "INMAB6", "INMAE6", "INMAH1", "INMAI6", "INMAL1", "INMAP1", "INMAQ6", "INMAS6", "INMBC6", "INMBD6", "INMBS6", "INMCI1", "INMDA1", "INMDD6", "INMDE6", "INMDG6", "INMDK1", "INMDP1", "INMDU6", "INMDV1", "INMDW1", "INMEA6", "INMEC6", "INMGHB", "INMGR1", "INMHA1", "INMHDB", "INMHE1", "INMHGB", "INMHN2", "INMKCB", "INMKD6", "INMLI1", "INMLP1", "INMLW1", "INMNB2", "INMNR1", "INMNUB", "INMNW1", "INMOH4", "INMOR2", "INMPC1", "INMPR6", "INMQK6", "INMRA1", "INMRD1", "INMREB", "INMRG4", "INMRJ6", "INMRM1", "INMSR6", "INMTW1", "INMUC6", "INMUL6", "INMUN1", "INMUR1", "INMUZ6", "INMWA6", "INMYB1", "INMYL6", "INMYO6", "INMYQ4", "INMZA4", "INMZU4", "INNAG4", "INNAG6", "INNAN1", "INNAV1", "INNDA6", "INNDC4", "INNDG1", "INNDP1", "INNEE1", "INNEL1", "INNGB6", "INNGKB", "INNGO6", "INNGP6", "INNGRB", "INNGSB", "INNKI6", "INNKNB", "INNML1", "INNMTB", "INNNN6", "INNPGB", "INNPT1", "INNRP6", "INNSA1", "INNSK6", "INNTLB", "INNTVB", "INNUR6", "INNVB1", "INNVP1", "INNVT1", "INNVY4", "INNWP1", "INNYP6", "INOKH1", "INOMN4", "INOMU1", "INONJ1", "INPAB4", "INPAK6", "INPAN1", "INPAO6", "INPAP2", "INPAT4", "INPAV1", "INPAV2", "INPBD1", "INPBD4", "INPBLB", "INPDD1", "INPEK6", "INPGH4", "INPHBB", "INPID1", "INPIN1", "INPIT6", "INPKD6", "INPKR6", "INPMB1", "INPMP6", "INPMT6", "INPNB6", "INPNE6", "INPNF5", "INPNI6", "INPNJ1", "INPNK6", "INPNL6", "INPNM1", "INPNN1", "INPNP6", "INPNQ2", "INPNQ4", "INPNQ6", "INPNTB", "INPNU6", "INPNV6", "INPNY1", "INPNY4", "INPNY6", "INPPG6", "INPPJ1", "INPRD6", "INPRG1", "INPRK6", "INPRT1", "INPSH1", "INPSI6", "INPSN6", "INPSP6", "INPTL6", "INPTN1", "INPTPB", "INPUA6", "INPUE6", "INPUI6", "INPUL1", "INPUM6", "INPUN6", "INPUR1", "INPUT4", "INPVL6", "INPVS6", "INPWL6", "INPYB4", "INPYS6", "INQRP6", "INQUI1", "INRAI6", "INRAJ4", "INRAJ6", "INRAM1", "INRDP2", "INREA6", "INRED1", "INREW4", "INRGBB", "INRGH4", "INRGJ2", "INRGT1", "INRGUB", "INRJA4", "INRJI4", "INRJN6", "INRJP1", "INRJR1", "INRKG1", "INRMD4", "INRML6", "INRNC5", "INRNG2", "INRNR1", "INRPL6", "INRPR4", "INRPR6", "INRPU5", "INRRI1", "INRRK4", "INRTC1", "INRTC4", "INRTM6", "INRUP4", "INRVD1", "INRWR1", "INRXLB", "INSABB", "INSAC6", "INSAJ6", "INSAL1", "INSAS6", "INSAU6", "INSBC6", "INSBH1", "INSBI6", "INSBK6", "INSBL6", "INSBW6", "INSBZ1", "INSCH6", "INSGF6", "INSHI1", "INSHL4", "INSHP1", "INSIK1", "INSJR6", "INSKD6", "INSKPB", "INSLL6", "INSLR2", "INSLRB", "INSLT6", "INSLV4", "INSMK6", "INSMPB", "INSMR1", "INSNA6", "INSNBB", "INSNF6", "INSNG2", "INSNI6", "INSNLB", "INSNN6", "INSNR6", "INSNS6", "INSPC6", "INSPE6", "INSRE6", "INSRK6", "INSRV1", "INSSE4", "INSTFB", "INSTIB", "INSTM6", "INSTP1", "INSTRB", "INSTT6", "INSTU6", "INSTV1", "INSTV4", "INSTV6", "INSWD1", "INSXE6", "INSXR4", "INSXR5", "INSXV4", "INSXV6", "INTAD1", "INTAS6", "INTBC6", "INTBM6", "INTBP6", "INTBS6", "INTBT6", "INTCR6", "INTDE6", "INTEI4", "INTEL1", "INTEN6", "INTEZ4", "INTGN6", "INTHA6", "INTHL1", "INTHO6", "INTIR4", "INTIV1", "INTJA1", "INTJPB", "INTJV4", "INTKD2", "INTKD6", "INTKNB", "INTLG6", "INTLT6", "INTMI6", "INTMP1", "INTMX6", "INTNA1", "INTNC6", "INTND1", "INTNGB", "INTNI6", "INTNK1", "INTNS6", "INTPH1", "INTPJ6", "INTPN1", "INTRA1", "INTRL6", "INTRP1", "INTRV4", "INTRZ4", "INTSI6", "INTTP6", "INTTS1", "INTUI6", "INTUN1", "INTUP6", "INTUT1", "INTUT6", "INTVC6", "INTVT6", "INTYR1", "INUDI6", "INUDN6", "INUDR4", "INUDR6", "INUDZ6", "INUKL6", "INULPB", "INULW1", "INUMB1", "INUMR1", "INURF6", "INURG6", "INURI6", "INURT6", "INUTN1", "INVAD1", "INVAL6", "INVAP1", "INVEN1", "INVEP1", "INVGA4", "INVGA5", "INVGR6", "INVKH6", "INVKM1", "INVLD6", "INVLN6", "INVLR6", "INVNG1", "INVNS4", "INVNS5", "INVNS6", "INVPI6", "INVRD1", "INVRU1", "INVSA6", "INVSI1", "INVSK6", "INVSP6", "INVSV1", "INVTC6", "INVTZ1", "INVTZ4", "INVTZ6", "INVVA1", "INVYD1", "INVZJ1", "INVZM6", "INVZR6", "INWAL6", "INWFD6", "INWFI6", "INWFT6", "INWGC4", "INWRR6", "INYMA6", "INYNA6", "INYNK6", "INYNL6", "INYNM6", "INYNT6", "INZIP6"],
      "description": "Port Code"
    },
    "ForCurList": {
      "type": "string",
      "maxLength": 3,
      "minLength":3,
      "enum": ["BDT", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BOV", "BRL", "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHE", "CHF", "CHW", "CLF", "CLP", "CNY", "COP", "COU", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MXV", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STN", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "USN", "UYI", "UYU", "UYW", "UZS", "VES", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XBA", "XBB", "XBC", "XBD", "XCD", "XDR", "XOF", "XPD", "XPF", "XPT", "XSU", "XTS", "XUA", "XXX", "YER", "ZAR", "ZMW", "ZWL",
        "bdt", "aed", "afn", "all", "amd", "ang", "aoa", "ars", "aud", "awg", "azn", "bam", "bbd", "bdt", "bgn", "bhd", "bif", "bmd", "bnd", "bob", "bov", "brl", "bsd", "btn", "bwp", "byn", "bzd", "cad", "cdf", "che", "chf", "chw", "clf", "clp", "cny", "cop", "cou", "crc", "cuc", "cup", "cve", "czk", "djf", "dkk", "dop", "dzd", "egp", "ern", "etb", "eur", "fjd", "fkp", "gbp", "gel", "ghs", "gip", "gmd", "gnf", "gtq", "gyd", "hkd", "hnl", "hrk", "htg", "huf", "idr", "ils", "inr", "iqd", "irr", "isk", "jmd", "jod", "jpy", "kes", "kgs", "khr", "kmf", "kpw", "krw", "kwd", "kyd", "kzt", "lak", "lbp", "lkr", "lrd", "lsl", "lyd", "mad", "mdl", "mga", "mkd", "mmk", "mnt", "mop", "mru", "mur", "mvr", "mwk", "mxn", "mxv", "myr", "mzn", "nad", "ngn", "nio", "nok", "npr", "nzd", "omr", "pab", "pen", "pgk", "php", "pkr", "pln", "pyg", "qar", "ron", "rsd", "rub", "rwf", "sar", "sbd", "scr", "sdg", "sek", "sgd", "shp", "sll", "sos", "srd", "ssp", "stn", "svc", "syp", "szl", "thb", "tjs", "tmt", "tnd", "top", "try", "ttd", "twd", "tzs", "uah", "ugx", "usd", "usn", "uyi", "uyu", "uyw", "uzs", "ves", "vnd", "vuv", "wst", "xaf", "xag", "xau", "xba", "xbb", "xbc", "xbd", "xcd", "xdr", "xof", "xpd", "xpf", "xpt", "xsu", "xts", "xua", "xxx", "yer", "zar", "zmw", "zwl"],
      "description": "Foreign Currency"
    },
    "CntCodeList": {
      "type": "string",
      "maxLength": 2,
      "minLength": 2,
      "enum": ["AD", "AE", "AF", "AG", "AI", "AL", "AM", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "FI", "FJ", "FK", "FM", "FO", "FR", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV", "SX", "SY", "SZ", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "YE", "YT", "ZA", "ZM", "ZW",
        "ad", "ae", "af", "ag", "ai", "al", "am", "ao", "aq", "ar", "as", "at", "au", "aw", "ax", "az", "ba", "bb", "bd", "be", "bf", "bg", "bh", "bi", "bj", "bl", "bm", "bn", "bo", "bq", "br", "bs", "bt", "bv", "bw", "by", "bz", "ca", "cc", "cd", "cf", "cg", "ch", "ci", "ck", "cl", "cm", "cn", "co", "cr", "cu", "cv", "cw", "cx", "cy", "cz", "de", "dj", "dk", "dm", "do", "dz", "ec", "ee", "eg", "eh", "er", "es", "et", "fi", "fj", "fk", "fm", "fo", "fr", "ga", "gb", "gd", "ge", "gf", "gg", "gh", "gi", "gl", "gm", "gn", "gp", "gq", "gr", "gs", "gt", "gu", "gw", "gy", "hk", "hm", "hn", "hr", "ht", "hu", "id", "ie", "il", "im", "in", "io", "iq", "ir", "is", "it", "je", "jm", "jo", "jp", "ke", "kg", "kh", "ki", "km", "kn", "kp", "kr", "kw", "ky", "kz", "la", "lb", "lc", "li", "lk", "lr", "ls", "lt", "lu", "lv", "ly", "ma", "mc", "md", "me", "mf", "mg", "mh", "mk", "ml", "mm", "mn", "mo", "mp", "mq", "mr", "ms", "mt", "mu", "mv", "mw", "mx", "my", "mz", "na", "nc", "ne", "nf", "ng", "ni", "nl", "no", "np", "nr", "nu", "nz", "om", "pa", "pe", "pf", "pg", "ph", "pk", "pl", "pm", "pn", "pr", "ps", "pt", "pw", "py", "qa", "re", "ro", "rs", "ru", "rw", "sa", "sb", "sc", "sd", "se", "sg", "sh", "si", "sj", "sk", "sl", "sm", "sn", "so", "sr", "ss", "st", "sv", "sx", "sy", "sz", "tc", "td", "tf", "tg", "th", "tj", "tk", "tl", "tm", "tn", "to", "tr", "tt", "tv", "tw", "tz", "ua", "ug", "um", "us", "uy", "uz", "va", "vc", "ve", "vg", "vi", "vn", "vu", "wf", "ws", "ye", "yt", "za", "zm", "zw"],
      "description": "Country"
    },
    "ExpDtlsSection": {
      "type": "object",
      "properties": {
        "ExpCat": {
          "type": "string",
          "minLength": 3,
          "maxLength": 3,
          "enum": ["DIR", "DEM", "SEZ", "SED", "dir", "dem", "sez", "sed"],
          "description": "Export Category: DIR-DIRECT, DEM-DEEMED, SEZSEZ, SED-SEZ DEVELOPER"
        },
        "WthPay": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1,
          "enum": ["Y", "N", "y", "n"],
          "description": "Export Payment - Y for With Payment, N for Without Payment"
        },
        "ShipBNo": {
          "type": "string",
          "minLength": 1,
          "maxLength": 16,
          "description": "Shipping Bill No."
        },
        "ShipBDt": {
          "type": "string",
          "maxLength": 10,
          "inLength": 10,
          "pattern": "[2][0][1-2][0-9]-[0-1][0-9]-[0-3][0-9]",
          "description": "Shipping Bill Date"
        },
        "Port": {
          "$ref": "#/definitions/portList"
        },
        "InvForCur": {
          "type": "number",
          "minimum": 0,
          "maxLength": 17,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "description": "Total Invoice value in Foreign Currency"
        },
        "ForCur": {
          "$ref": "#/definitions/ForCurList"
        },
        "CntCode": {
          "$ref": "#/definitions/CntCodeList"
        }
      },
      "required": ["ExpCat", "WthPay", "InvForCur", "ForCur", "CntCode"]
    },
    "commonMIS": {
      "$ref": "#/definitions/two50Length",
      "description": "Additional fields for internal MIS purposes"
    },
    "MisColumnsDtls":{
      "type": "object",
      "properties": {
        "Bu": {
          "$ref": "#/definitions/two50Length",
          "description": "Business Unit to which this document pertains"
        },
        "Sbu": {
          "$ref": "#/definitions/two50Length",
          "description": "Sub Business Unit to which this document pertains"
        },
        "Location": {
          "$ref": "#/definitions/two50Length",
          "description": "Location to which this document pertains"
        },
        "User": {
          "$ref": "#/definitions/two50Length",
          "description": "User to which this document pertatins"
        },
        "CompanyCode": {
          "$ref": "#/definitions/two50Length",
          "description": "Company Code"
        },
        "CompanyName": {
          "$ref": "#/definitions/two50Length",
          "description": "Company Name"
        },
        "TrackingNo": {
          "$ref": "#/definitions/two50Length",
          "description": "Tracking Number for internal purposes"
        },
        "TransactionCount": {
          "type": "integer",
          "minLength": 0,
          "maxLength": 5,
          "minimum": 0,
          "maximum": 99999,
          "description": "Total line items in the document for tracking purposes"
        },
        "GlAccount": {
          "$ref": "#/definitions/two50Length",
          "description": "GL Account"
        },
        "EwbNo": {
          "type": "integer",
          "minimum": 100000000000,
          "maximum": 999999999999,
          "description": "E-way bill No"
        },
        "ReturnPeriod": {
          "type": "string",
          "minLength": 5,
          "maxLength": 6,
          "description": "GST return month in which this transaction to be considered"
        },
        "Mis11": {
          "$ref": "#/definitions/commonMIS"
        },
        "Mis12": {
          "$ref": "#/definitions/commonMIS"
        },
        "Mis13": {
          "$ref": "#/definitions/commonMIS"
        },
        "Mis14": {
          "$ref": "#/definitions/commonMIS"
        },
        "Mis15": {
          "$ref": "#/definitions/commonMIS"
        },  
        "Mis16": {
          "$ref": "#/definitions/commonMIS"
        },  
        "Mis17": {
          "$ref": "#/definitions/commonMIS"
        },
        "Mis18": {
          "$ref": "#/definitions/commonMIS"
        },
        "Mis19": {
          "$ref": "#/definitions/commonMIS"
        },
        "Mis20": {
          "$ref": "#/definitions/commonMIS"
        },
        "Mis21": {
          "$ref": "#/definitions/commonMIS"
        },  
        "Mis22": {
          "$ref": "#/definitions/commonMIS"
        },
        "Mis23": {
          "$ref": "#/definitions/commonMIS"
        },
        "Mis24": {
          "$ref": "#/definitions/commonMIS"
        },
        "Mis25": {
          "$ref": "#/definitions/commonMIS"
        },
        "Mis26": {
          "$ref": "#/definitions/commonMIS"
        },
        "Mis27": {
          "$ref": "#/definitions/commonMIS"
        },
        "Mis28": {
          "$ref": "#/definitions/commonMIS"
        },
        "Mis29": {
          "$ref": "#/definitions/commonMIS"
        },
        "Mis30": {
          "$ref": "#/definitions/commonMIS"
        }
      }
    },
    "commonFU": {
      "$ref": "#/definitions/two50Length",
      "description": "Additional fields for future use"
    },
    "FuColumnsDtls": {
      "type": "object",
      "properties": {
        "Fu11": {
          "$ref": "#/definitions/commonFU"
        },
        "Fu12": {
          "$ref": "#/definitions/commonFU"
        },
        "Fu13": {
          "$ref": "#/definitions/commonFU"
        },
        "Fu14": {
          "$ref": "#/definitions/commonFU"
        },
        "Fu15": {
          "$ref": "#/definitions/commonFU"
        },
        "Fu16": {
          "$ref": "#/definitions/commonFU"
        },
        "Fu17": {
          "$ref": "#/definitions/commonFU"
        },
        "Fu18": {
          "$ref": "#/definitions/commonFU"
        },
        "Fu19": {
          "$ref": "#/definitions/commonFU"
        },
        "Fu20": {
          "$ref": "#/definitions/commonFU"
        },
        "Fu21": {
          "$ref": "#/definitions/commonFU"
        },
        "Fu22": {
          "$ref": "#/definitions/commonFU"
        },
        "Fu23": {
          "$ref": "#/definitions/commonFU"
        },
        "Fu24": {
          "$ref": "#/definitions/commonFU"
        },
        "Fu25": {
          "$ref": "#/definitions/commonFU"
        },
        "Fu26": {
          "$ref": "#/definitions/commonFU"
        },
        "Fu27": {
          "$ref": "#/definitions/commonFU"
        },
        "Fu28": {
          "$ref": "#/definitions/commonFU"
        },
        "Fu29": {
          "$ref": "#/definitions/commonFU"
        },
        "Fu30": {
          "$ref": "#/definitions/commonFU"
        }
      }
    },
    "TransportDtlsSection": {
      "type": "object",
      "properties": {
        "TransporterId": {
          "type": "string",
          "maxLength": 15,
          "minLength": 0,
          "pattern": "[0-9]{2}[0-9|A-Z]{13}|^$",
          "description": "Transporter ID"
        },
        "DistanceKm": {
          "type": "integer",
          "minimum": 0,
          "maximum": 3000,
          "description": "Distance (Km)"
        },
        "TransporterName": {
          "type": "string",
          "maxLength": 100,
          "minLength": 0,
          "description": "Transporter Name"
        },
        "TransMode": {
          "type": "string",
          "maxLength": 4,
          "enum": ["ROAD", "RAIL", "AIR", "SHIP", "road", "rail", "air", "ship"],
          "description": "Trans Mode"
        },
        "TransDocNo": {
          "type": "string",
          "maxLength": 15,
          "minLength": 0,
          "description": "Trans Doc No"
        },
        "TransDocDate": {
          "type": "string",
          "maxLength": 10,
          "minLength": 10,
          "pattern": "[2][0][1-2][0-9]-[0-1][0-9]-[0-3][0-9]",
          "description": "Trans Doc Date"
        },
        "VehicleNo": {
          "type": "string",
          "maxLength": 15,
          "minLength": 7,
          "description": "Vehicle No"
        },
        "VehicleType": {
          "type": "string",
          "maxLength": 250,
          "minLength": 0,
          "enum": ["REGULAR", "OVER DIMENSIONAL CARGO", "regular", "over dimensional cargo"],
          "description": "Vehicle Type"
        }
      }
    }
  },
  "properties": {
    "User_GSTIN": {
      "type": "string",
      "maxLength": 15,
      "minLength": 15,
      "pattern": "[0-9]{2}[0-9|A-Z]{13}"
    },
    "TaxSch": {
      "enum": ["GST"],
      "type": "string",
      "maxLength": 3,
      "minLength": 0
    },
    "Version": {
      "maxLength": 4,
      "minLength": 0,
      "type": "string"
    },
    "Irn": {
      "type": "string",
      "maxLength": 64,
      "minLength": 46,
      "description": "Invoice Reference No."
    },
    "TranDtls": {
      "$ref": "#/definitions/TranDtlsSection"
    },
    "DocDtls": {
      "$ref": "#/definitions/DocDtlsSection"
    },
    "SellerDtls": {
      "$ref": "#/definitions/SellerDtlsSection"
    },
    "BuyerDtls": {
      "$ref": "#/definitions/BuyerDtlsSection"
    },
    "DispDtls": {
      "$ref": "#/definitions/DispDtlsSection"
    },
    "ShipDtls": {
      "$ref": "#/definitions/ShipDtlsSection"
    },
    "ItemList":{
      "items":{
        "$ref": "#/definitions/InvoiceItemDetails"
      },
      "type": "array"
    },
    "ValDtls": {
      "$ref": "#/definitions/ValDtlsSection"
    },
    "PayDtls": {
      "$ref": "#/definitions/PayDtlsSection"
    },
    "RefDtls": {
      "$ref": "#/definitions/RefDtlsSection"
    },
    "ExpDtls": {
      "$ref": "#/definitions/ExpDtlsSection"
    },
    "MisColumns":{
      "$ref": "#/definitions/MisColumnsDtls"
    },
    "FuColumns": {
      "$ref": "#/definitions/FuColumnsDtls"
    },
    "TransportDtls": {
      "$ref": "#/definitions/TransportDtlsSection"
    },
    "is_irn":{
      "type": "string",
      "minLength": 0,
      "maxLength": 1,
      "enum": ["", "Y", "N", "y", "n"],
      "description": "Is IRN"
    },
    "is_ewb": {
      "type": "string",
      "minLength": 0,
      "maxLength": 1,
      "enum": ["", "Y", "N", "y", "n"],
      "description": "IS EWB"
    }
  },
  "required": ["TaxSch", "TranDtls", "DocDtls", "SellerDtls", "BuyerDtls", "ItemList",
    "ValDtls"],
  "type": "object",
  "allOf":[
    {
      "if":{
        "properties": {
          "TranDtls": {"properties": {"Catg": {"enum": ["EXP", "exp"]}}
          }
        }
      },
      "then":{
        "required": ["ExpDtls"]       
      }
    },
    {
      "if":{
        "properties": {
          "TranDtls": {"properties": {"Typ": {"enum": ["DIS", "dis"]}}
          }
        }
      },
      "then":{
        "required": ["DispDtls"]  
      }
    },
    {
      "if":{
        "properties": {
          "TranDtls": {"properties": {"Typ": {"enum": ["SHP", "shp"]}}
          }
        }
      },
      "then":{
        "required": ["ShipDtls"]     
      }
    }
  ],
}
# HSN SCHEMA
HSN_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "definitions": {
        "InvoiceItemDetails": {
            "properties": {
                "HsnCd": {
                    "type": "string",
                    "minLength": 4,
                    "maxLength": 8,
          "pattern": "[0-8][0-9][0-9]{2,6}|[0-9][0-8][0-9]{2,6}",
                    "description": "HSN Code"
                }
            },
            "required": ["HsnCd"],
            "type": "object"
        },
    },
    "properties": {
        "ItemList": {
            "items": {
                "$ref": "#/definitions/InvoiceItemDetails"
            },
            "type": "array"
        }
    },
    "required": ["ItemList"],
    "type": "object"
}
# Check Gst amount exist or not schema
GST_AMT_CHCK_SCHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "definitions": {
    "InvoiceItemDetails": {
      "properties": {
        "AssAmt": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "description": "Assessable Amount (Total Amount -Discount + Other charges)"
        },
        "CesNonAdVal": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "description": "Cess Non-Advol Amount"
        },
        "StateCes": {
          "type": "number",
          "maximum": 999.999,
          "multipleOf": 0.001,
          "description": "State CESS Rate",
          "minimum": 0
        },
        "TotItemVal": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "description": "Total Item Value : Assessable Amount [1 + (CGST Rate + SGST Rate + Cess Rate + State Cess Rate)] + Cess NonAdvol Amount "
        },
        "IgstAmt": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "description": "IGST Amount as per item"
        },
        "CgstAmt": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "description": "CGST Amount as per item"
        },
        "SgstAmt": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "description": "SGST Amount as per item"
        },
        "CessAmt": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "description": "CESS Amount as per item"
        },
      },
      "required": ["AssAmt", "IgstAmt", "CgstAmt", "SgstAmt", "TotItemVal", "CesNonAdVal", "StateCes", "CessAmt"],
      "type": "object"
    }
  },
  "properties": {
    "ItemList": {
      "items": {
        "$ref": "#/definitions/InvoiceItemDetails"
      },
      "type": "array"
    }
  },
  "required": ["ItemList"],
  "type": "object"
}
# check gst rate exist or not schema
GST_RT_CHCK_SCHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "definitions": {
    "InvoiceItemDetails": {
      "properties": {
        "AssAmt": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "maxLength": 17,
          "description": "Assessable Amount (Total Amount -Discount + Other charges)"
        },
        "CgstRt": {
          "type": "number",
          "maximum": 999.999,
          "minimum": 0,
          "description": "CGSTRate"
        },
        "SgstRt": {
          "type": "number",
          "maximum": 999.999,
          "minimum": 0,
          "description": "SGSTRate"
        },
        "IgstRt": {
          "type": "number",
          "maximum": 999.999,
          "minimum": 0,
          "description": "IGSTRate"
        },
        "CesRt": {
          "type": "number",
          "maximum": 999.999,
          "multipleOf": 0.001,
          "description": "CESSRate",
          "minimum": 0
        },
        "CesNonAdVal": {
          "type": "number",
          "minimum": 0,
          "maximum": 99999999999999.99,
          "multipleOf": 0.01,
          "maxLength": 17,
          "description": "Cess Non-Advol Amount"
        },
        "StateCes": {
          "type": "number",
          "maximum": 999.999,
          "multipleOf": 0.001,
          "description": "State CESS Rate",
          "minimum": 0
        }
      },
      "required": ["CgstRt", "SgstRt", "IgstRt", "CesRt", "CesNonAdVal", "StateCes", "TotItemVal", "AssAmt"],
      "type": "object"
    }
  },
  "properties": {
    "ItemList": {
      "items": {
        "$ref": "#/definitions/InvoiceItemDetails"
      },
      "type": "array"
    }
  },
  "required": ["ItemList"],
  "type": "object"
}
