'''
Here we are creating async database connection


#The purpose of this file is to make database connection
'''
from __future__ import print_function
import time
import logging
import psycopg2
import psycopg2.extras
from module.util.dao import SQSService
from settings.configuration import PROCESS_NAME, SQS_TEMPLATE
LOGGER = logging.getLogger("einvoice_app")

#Helper function
#Connecting to the database
def create_connection(database):
    # pylint: disable-msg=W0703
    '''
    Input  -
       params: database - The name of the database to be connected
    Output - Connected to the database
    '''
    conn = psycopg2.connect(database=database["database_name"], user=database["user"],\
        password=database["password"], host=database["host"],\
        port=database["port"])
    return conn

#Helper function
#Creating dict cursor object
def get_dict_cursor(conn):
    # pylint: disable-msg=W0703
    '''
    Input  -
       params: conn - Connection object
    Output - Dict cursor object is created
    '''
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    return cursor

def exist_conn_closed(conn):
    '''
        checking if connection is not closed then closed the connection
        Input -
        param: conn - Database connection object
    '''
    if conn and conn.closed == 0:
        conn.close()

def exist_cur_conn_closed(conn, cursor):
    '''
    closing database connection and cursor
    Input -
        params: conn - Database connection object
        params: cursor -Database cursor object
    '''
    cursor.close()
    conn.close()

def fetch_row(cursor, query):
    '''
    here we are getting single row from table
    params - cursor: database dict cursor
    params - query: select query
    '''
    cursor.execute(query)
    return cursor.fetchone()

def irn_insert_query_execute(irn_master_query, irn_master_data, irn_dtls_query,\
    irn_dtls_list, irn_mis_dtls_query, irn_mis_dtls_list, database, customer_id,\
    email_ids):
    # pylint: disable-msg=W0703
    '''
    it is async method.
    Here we are inserting the data to table irn_master, irn_details, irn_custom
    params - irn_master_query: insert query for irn_master table
    params - irn_master_data: data which insert into irn_master table
    params - database: client database credential,
    params - irn_details_insert_query: insert query for irn_details table
    params - irn_mis_dtls_query: insert query for inr_mis_details table
    params - irn_mis_dtls_list: params - irn_mis_dtls_list appending the
        data to irn_mis_dtls_list
    params - irn_details_list: data which insert into irn_details table
    params - customer_id: client id
    params - email_ids: email id
    '''
    # creating database connection
    start_time = time.time()
    conn = None
    try:
        conn = create_connection(database)
        cursor = get_dict_cursor(conn)
        # inserting data to inr_master_table
        cursor.executemany(irn_master_query, irn_master_data)
        if irn_dtls_list:
            cursor.executemany(irn_dtls_query, irn_dtls_list)
        if irn_mis_dtls_list:
            cursor.executemany(irn_mis_dtls_query, irn_mis_dtls_list)
        conn.commit()
        exist_cur_conn_closed(conn, cursor)
    except Exception as error:
        exist_conn_closed(conn)
        LOGGER.info("Getting Exception on insertion operation")
        LOGGER.error(f"Exception -> {error}", exc_info=True)
        SQSService.exception_sending(customer_id, PROCESS_NAME["IRN_GENERATE"],\
            SQS_TEMPLATE['EXCEPTION'], email_ids, error_message=str(error))
    LOGGER.info("total time taken irn_insert -> %s",\
        format((time.time() - start_time) * 1000, '.2f'))

def upload_insert_execute(upload_data, upload_query, conn, cursor, database):
    # pylint: disable-msg=W0703
    '''
    it is async method.
    Here we are inserting the data to table upload.
    params - upload_data: upload table data
    params - upload_query: upload insert query
    params - database: database credential
    '''
    start_time = time.time()
    # inserting data to upload table
    if not conn:
        conn = create_connection(database)
        cursor = get_dict_cursor(conn)
    elif conn.closed != 0:
        conn = create_connection(database)
        cursor = get_dict_cursor(conn)
    cursor.execute(upload_query, upload_data)
    conn.commit()
    LOGGER.info("total time taken upload_insert -> %s",\
        format((time.time() - start_time) * 1000, '.2f'))
