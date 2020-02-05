'''
all redis releated work are here
'''
import logging
import redis
import orjson
from .configuration import REDIS_CONFIG
LOGGER = logging.getLogger("einvoice_app")

class RedisCache:
    '''
    Redis connection
    '''
    def __init__(self):
        '''
        initiate object
        '''
        pass

    def __str__(self):
        '''
        object reperesentation
        '''
        print("RedisCache object")

    @staticmethod
    def get_cache(key, env):
        # pylint: disable-msg=W0703
        # pylint: disable-msg=W0613
        '''
        Here we are read client configuration from s3 bucket
        params - key : redis key
        params - env: env value
        '''
        cache = {}
        try:
            client = redis.Redis(**REDIS_CONFIG[env], ssl=True)
            get_data = client.get(key)
            if get_data:
                cache = orjson.loads(get_data)
        except Exception as error:
            LOGGER.error(str(error), exc_info=True)
        return cache

    @staticmethod
    def get_client_config(customer_id, env):
        '''
        Here we are read client configuration from s3 bucket
        params - customer_id: client id
        params - env: environment value
        '''
        key = f"{customer_id}_e-invoice_etl_cache"
        return RedisCache.get_cache(key, env)

    @staticmethod
    def get_master_config(customer_id, env):
        '''
        Here we are getting master config from cache
        params - customer_id: client id
        params - env: environment value
        '''
        key = f"{customer_id}_etl_master_config"
        return RedisCache.get_cache(key, env)
