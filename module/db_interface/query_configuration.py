'''
Insert Query
'''
IRN_MASTER_QUERY = ("INSERT INTO demo.irn_master (user_gstin, irn, trandtls_catg, "\
    "trandtls_regrev, trandtls_typ, trandtls_ecmtrn, trandtls_ecmgstin, trandtls_outwardinward, "\
    "trandtls_subtype, trandtls_subtypedescription, trandtls_pos, trandtls_claimingrefund, "\
    "trandtls_diffpercentage, trandtls_taxability, trandtls_interintra, docdtls_typ, docdtls_no, "\
    "docdtls_dt, docdtls_orginvno, docdtls_orginvdt, docdtls_reasonforcndn, expdtls_expcat, "\
    "expdtls_wthpay, expdtls_shipbno, expdtls_shipbdt, expdtls_port, expdtls_invforcur, "\
    "expdtls_forcur, expdtls_cntcode, bu, sbu, location, \"user\", companycode, companyname, "\
    "trackingno, transactioncount, glaccount, ewbno, returnperiod, transportdtls_transporterid, "\
    "transportdtls_distancekm, transportdtls_transportername, transportdtls_transmode, "\
    "transportdtls_transdocno, transportdtls_transdocdate, transportdtls_vehicleno, "\
    "transportdtls_vehicletype, sellerdtls_gstin, sellerdtls_trdnm, sellerdtls_bno, "\
    "sellerdtls_bnm, sellerdtls_flno, sellerdtls_loc, sellerdtls_dst, sellerdtls_pin, "\
    "sellerdtls_stcd, sellerdtls_ph, sellerdtls_em, sellerdtls_suppliercode, buyerdtls_gstin, "\
    "buyerdtls_trdnm, buyerdtls_bno, buyerdtls_bnm, buyerdtls_flno, buyerdtls_loc, buyerdtls_dst,"\
    "buyerdtls_pin, buyerdtls_stcd, buyerdtls_ph, buyerdtls_em, buyerdtls_customercode, "\
    "dispdtls_gstin, dispdtls_trdnm, dispdtls_bno, dispdtls_bnm, dispdtls_flno, dispdtls_loc, "\
    "dispdtls_dst, dispdtls_pin, dispdtls_stcd, dispdtls_ph, dispdtls_em, shipdtls_gstin, "\
    "shipdtls_trdnm, shipdtls_bno, shipdtls_bnm, shipdtls_flno, shipdtls_loc, shipdtls_dst, "\
    "shipdtls_pin, shipdtls_stcd, shipdtls_ph, shipdtls_em, valdtls_assval, valdtls_cgstval, "\
    "valdtls_sgstval, valdtls_igstval, valdtls_cesval, valdtls_stcesval, valdtls_cesnonadval, "\
    "valdtls_disc, valdtls_othchrg, valdtls_totinvval, refdtls_invrmk, refdtls_invstdt, "\
    "refdtls_invenddt, refdtls_precinvno, refdtls_precinvdt, refdtls_recadvref, refdtls_tendref, "\
    "refdtls_contrref, refdtls_extref, refdtls_projref, refdtls_poref, refdtls_vendorporefdt, "\
    "refdtls_accountingdocno, refdtls_accountingdocdt, refdtls_sono, refdtls_sodt, paydtls_nam, "\
    "paydtls_mode, paydtls_fininsbr, paydtls_payterm, paydtls_payinstr, paydtls_crtrn, "\
    "paydtls_dirdr, paydtls_crday, paydtls_balamt, paydtls_payduedt, paydtls_acctdet, is_irn, "\
    "is_ewb, is_cancel, mis_action, nic_request_payload, nic_header, nic_status, nic_gen_mode, "\
    "nic_document_status_created_date, nic_response_encoded, nic_response_plaintext_json, "\
    "nic_response_created_date, nic_response_status, nic_response_errorcode, ackno, ackdt, "\
    "signedinvoice, signedqrcode, created_by, created_date, updated_date, updated_by, is_active, "\
    "data_source, comments, update_history, load_id, udid, bu_id, sbu_id, location_id, "\
    "gstin_id, company_id, response_body, validation_remark, is_exclude, nic_error_details, "\
    "nic_qr_image, report_url, pwc_response_message, pwc_response_validation_status, "\
    "pwc_response_validation_remarks, irp_response_message, irp_response_error, irn_status, "\
    "pwc_response_status, exclude_reason) VALUES(%(user_gstin)s, %(irn)s, "\
    "%(trandtls_catg)s, %(trandtls_regrev)s, %(trandtls_typ)s, %(trandtls_ecmtrn)s, "\
    "%(trandtls_ecmgstin)s, %(trandtls_outwardinward)s, %(trandtls_subtype)s, "\
    "%(trandtls_subtypedescription)s, %(trandtls_pos)s, %(trandtls_claimingrefund)s, "\
    "%(trandtls_diffpercentage)s, %(trandtls_taxability)s, %(trandtls_interintra)s, "\
    "%(docdtls_typ)s, %(docdtls_no)s, %(docdtls_dt)s, %(docdtls_orginvno)s, "\
    "%(docdtls_orginvdt)s, %(docdtls_reasonforcndn)s, %(expdtls_expcat)s, %(expdtls_wthpay)s, "\
    "%(expdtls_shipbno)s, %(expdtls_shipbdt)s, %(expdtls_port)s, %(expdtls_invforcur)s, "\
    "%(expdtls_forcur)s, %(expdtls_cntcode)s, %(bu)s, %(sbu)s, %(location)s, %(user)s, "\
    "%(companycode)s, %(companyname)s, %(trackingno)s, %(transactioncount)s, %(glaccount)s, "\
    "%(ewbno)s, %(returnperiod)s, %(transportdtls_transporterid)s, %(transportdtls_distancekm)s, "\
    "%(transportdtls_transportername)s, %(transportdtls_transmode)s, "\
    "%(transportdtls_transdocno)s, %(transportdtls_transdocdate)s, %(transportdtls_vehicleno)s, "\
    "%(transportdtls_vehicletype)s, %(sellerdtls_gstin)s, %(sellerdtls_trdnm)s, "\
    "%(sellerdtls_bno)s, %(sellerdtls_bnm)s, %(sellerdtls_flno)s, %(sellerdtls_loc)s, "\
    "%(sellerdtls_dst)s, %(sellerdtls_pin)s, %(sellerdtls_stcd)s, %(sellerdtls_ph)s, "\
    "%(sellerdtls_em)s, %(sellerdtls_suppliercode)s, %(buyerdtls_gstin)s, %(buyerdtls_trdnm)s, "\
    "%(buyerdtls_bno)s, %(buyerdtls_bnm)s, %(buyerdtls_flno)s, %(buyerdtls_loc)s, "\
    "%(buyerdtls_dst)s, %(buyerdtls_pin)s, %(buyerdtls_stcd)s, %(buyerdtls_ph)s, "\
    "%(buyerdtls_em)s, %(buyerdtls_customercode)s, %(dispdtls_gstin)s, %(dispdtls_trdnm)s, "\
    "%(dispdtls_bno)s, %(dispdtls_bnm)s, %(dispdtls_flno)s, %(dispdtls_loc)s, %(dispdtls_dst)s, "\
    "%(dispdtls_pin)s, %(dispdtls_stcd)s, %(dispdtls_ph)s, %(dispdtls_em)s, %(shipdtls_gstin)s, "\
    "%(shipdtls_trdnm)s, %(shipdtls_bno)s, %(shipdtls_bnm)s, %(shipdtls_flno)s, %(shipdtls_loc)s, "\
    "%(shipdtls_dst)s, %(shipdtls_pin)s, %(shipdtls_stcd)s, %(shipdtls_ph)s, %(shipdtls_em)s, "\
    "%(valdtls_assval)s, %(valdtls_cgstval)s, %(valdtls_sgstval)s, %(valdtls_igstval)s, "\
    "%(valdtls_cesval)s, %(valdtls_stcesval)s, %(valdtls_cesnonadval)s, %(valdtls_disc)s, "\
    "%(valdtls_othchrg)s, %(valdtls_totinvval)s, %(refdtls_invrmk)s, %(refdtls_invstdt)s, "\
    "%(refdtls_invenddt)s, %(refdtls_precinvno)s, %(refdtls_precinvdt)s, %(refdtls_recadvref)s, "\
    "%(refdtls_tendref)s, %(refdtls_contrref)s, %(refdtls_extref)s, %(refdtls_projref)s, "\
    "%(refdtls_poref)s, %(refdtls_vendorporefdt)s, %(refdtls_accountingdocno)s, "\
    "%(refdtls_accountingdocdt)s, %(refdtls_sono)s, %(refdtls_sodt)s, %(paydtls_nam)s, "\
    "%(paydtls_mode)s, %(paydtls_fininsbr)s, %(paydtls_payterm)s, %(paydtls_payinstr)s, "\
    "%(paydtls_crtrn)s, %(paydtls_dirdr)s, %(paydtls_crday)s, %(paydtls_balamt)s, "\
    "%(paydtls_payduedt)s, %(paydtls_acctdet)s, %(is_irn)s, %(is_ewb)s, %(is_cancel)s, "\
    "%(mis_action)s, %(nic_request_payload)s, %(nic_header)s, %(nic_status)s, %(nic_gen_mode)s, "\
    "%(nic_document_status_created_date)s, %(nic_response_encoded)s, "\
    "%(nic_response_plaintext_json)s, %(nic_response_created_date)s, %(nic_response_status)s, "\
    "%(nic_response_errorcode)s, %(ackno)s, %(ackdt)s, %(signedinvoice)s, %(signedqrcode)s, "\
    "%(created_by)s, %(created_date)s, %(updated_date)s, %(updated_by)s, %(is_active)s, "\
    "%(data_source)s, %(comments)s, %(update_history)s, %(load_id)s, %(udid)s, %(bu_id)s, "\
    "%(sbu_id)s, %(location_id)s, %(gstin_id)s, %(company_id)s, %(response_body)s, "\
    "%(validation_remark)s, %(is_exclude)s, %(nic_error_details)s, %(nic_qr_image)s, "\
    "%(report_url)s, %(pwc_response_message)s, %(pwc_response_validation_status)s, "\
    "%(pwc_response_validation_remarks)s, %(irp_response_message)s, %(irp_response_error)s, "\
    "%(irn_status)s, %(pwc_response_status)s, %(exclude_reason)s)")

# irn details query
IRN_DTLS_QUERY = ("INSERT INTO demo.irn_details(il_lineitem, il_itemcode, il_prdnm, il_prddesc, "\
    "il_hsncd, il_goodsservice, il_barcde, il_qty, il_freeqty, il_unit, il_unitprice, "\
    "il_totamt, il_cgstrt, il_sgstrt, il_igstrt, il_cesrt, il_cesnonadval, il_stateces, "\
    "il_totitemval, il_discount, il_othchrg, il_vat, il_centralexcise, il_stateexcise, "\
    "il_exportduty, il_valuebeforebcd, il_bcd, il_assamt, il_totalgstrate, il_cessnonadvolrt, "\
    "il_igstamt, il_cgstamt, il_sgstamt, il_cessamt, il_eligibilityitc, il_itcigst, "\
    "il_itccgst, il_itcsgst, il_itccess, il_natureofexpense, il_bchdtls_nm, il_bchdtls_expdt, "\
    "il_bchdtls_wrdt, il_mis1, il_mis2, il_mis3, il_mis4, il_mis5, il_mis6, il_mis7, il_mis8, "\
    "il_mis9, il_mis10, il_fu1, il_fu2, il_fu3, il_fu4, il_fu5, il_fu6, il_fu7, il_fu8, il_fu9, "\
    "il_fu10, il_created_by, il_created_date, il_updated_date, il_updated_by, il_is_active, "\
    "il_comments, il_load_id, il_udid, il_data_source, il_is_exclude, il_irn) "\
    "VALUES(%(il_lineitem)s, %(il_itemcode)s, %(il_prdnm)s, "\
    "%(il_prddesc)s, %(il_hsncd)s, %(il_goodsservice)s, %(il_barcde)s, %(il_qty)s, "\
    "%(il_freeqty)s, %(il_unit)s, %(il_unitprice)s, %(il_totamt)s, %(il_cgstrt)s, "\
    "%(il_sgstrt)s, %(il_igstrt)s, %(il_cesrt)s, %(il_cesnonadval)s, %(il_stateces)s, "\
    "%(il_totitemval)s, %(il_discount)s, %(il_othchrg)s, %(il_vat)s, %(il_centralexcise)s, "\
    "%(il_stateexcise)s, %(il_exportduty)s, %(il_valuebeforebcd)s, %(il_bcd)s, %(il_assamt)s, "\
    "%(il_totalgstrate)s, %(il_cessnonadvolrt)s, %(il_igstamt)s, %(il_cgstamt)s, %(il_sgstamt)s, "\
    "%(il_cessamt)s, %(il_eligibilityitc)s, %(il_itcigst)s, %(il_itccgst)s, %(il_itcsgst)s, "\
    "%(il_itccess)s, %(il_natureofexpense)s, %(il_bchdtls_nm)s, %(il_bchdtls_expdt)s, "\
    "%(il_bchdtls_wrdt)s, %(il_mis1)s, %(il_mis2)s, %(il_mis3)s, %(il_mis4)s, %(il_mis5)s, "\
    "%(il_mis6)s, %(il_mis7)s, %(il_mis8)s, %(il_mis9)s, %(il_mis10)s, %(il_fu1)s, %(il_fu2)s, "\
    "%(il_fu3)s, %(il_fu4)s, %(il_fu5)s, %(il_fu6)s, %(il_fu7)s, %(il_fu8)s, %(il_fu9)s, "\
    "%(il_fu10)s, %(il_created_by)s, %(il_created_date)s, %(il_updated_date)s, "\
    "%(il_updated_by)s, %(il_is_active)s, %(il_comments)s, %(il_load_id)s, %(il_udid)s, "\
    "%(il_data_source)s, %(il_is_exclude)s, %(il_irn)s)")
# IRN_MIS_DETAILS_TABLE INSERT QUERY
IRN_MIS_DTLS_QUERY = ("INSERT INTO demo.irn_mis_details(mis11, mis12, mis13, mis14, mis15, "\
    "mis16, mis17, mis18, mis19, mis20, mis21, mis22, mis23, mis24, mis25, mis26, mis27, "\
    "mis28, mis29, mis30, fu11, fu12, fu13, fu14, fu15, fu16, fu17, fu18, fu19, fu20, "\
    "fu21, fu22, fu23, fu24, fu25, fu26, fu27, fu28, fu29, fu30, created_by, created_date, "\
    "updated_date, updated_by, is_active, data_source, comments, update_history, load_id, "\
    "udid, is_exclude, irn) VALUES (%(mis11)s, %(mis12)s, %(mis13)s, %(mis14)s, %(mis15)s, "\
    "%(mis16)s, "\
    "%(mis17)s, %(mis18)s, %(mis19)s, %(mis20)s, %(mis21)s, %(mis22)s, %(mis23)s, %(mis24)s, "\
    "%(mis25)s, %(mis26)s, %(mis27)s, %(mis28)s, %(mis29)s, %(mis30)s, %(fu11)s, %(fu12)s, "\
    "%(fu13)s, %(fu14)s, %(fu15)s, %(fu16)s, %(fu17)s, %(fu18)s, %(fu19)s, %(fu20)s, "\
    "%(fu21)s, %(fu22)s, %(fu23)s, %(fu24)s, %(fu25)s, %(fu26)s, %(fu27)s, %(fu28)s, "\
    "%(fu29)s, %(fu30)s, %(created_by)s, %(created_date)s, %(updated_date)s, %(updated_by)s, "\
    "%(is_active)s, %(data_source)s, %(comments)s, %(update_history)s, %(load_id)s, %(udid)s, "\
    "%(is_exclude)s, %(irn)s)")
# upload insert query
UPLOAD_INSERT_QUERY = ("INSERT INTO demo.upload(id, load_id, source_system, category, data_type, "\
    "load_type, status, created_date, created_by, updated_date, updated_by, active, "\
    "einvoice_req_body, einvoice_res_body, company_id, company_name, state, file_name, "\
    "mapping, import_from_file, failed_quality, comments) VALUES(%(id)s, %(load_id)s, "\
    "%(source_system)s, %(category)s, %(data_type)s, %(load_type)s, %(status)s, "\
    "%(created_date)s, %(created_by)s, %(updated_date)s, %(updated_by)s, %(active)s, "\
    "%(einvoice_req_body)s, %(einvoice_res_body)s, %(company_id)s, %(company_name)s, %(state)s, "\
    "%(file_name)s, %(mapping)s, %(import_from_file)s, %(failed_quality)s, %(comments)s)")
