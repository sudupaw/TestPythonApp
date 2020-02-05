'''
export env variable from lambda env
'''
import os
import time
import logging
LOGGER = logging.getLogger("einvoice_app")

# use on prod/dev/qa
def get_env():
    '''
    creating database credential
    '''
    start_time = time.time()
    LOGGER.info("Start get_env")
    database = os.environ.get('db_name')
    host = os.environ.get('db_ipaddress')
    port = os.environ.get('port')
    user = os.environ.get('db_username')
    password = os.environ.get('db_password')
    db_dict = {}
    if database and host and port and user and password:
        db_dict['db_name'] = database
        db_dict['db_ipaddress'] = host
        db_dict['port'] = port
        db_dict['db_username'] = user
        db_dict['db_password'] = password
    LOGGER.info("End get_env time taken %s",\
        format((time.time() - start_time) * 1000, '.2f'))
    return db_dict
