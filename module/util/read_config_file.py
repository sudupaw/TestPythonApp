'''
#Reading the configuration file
'''
from __future__ import print_function
import logging
import boto3
import orjson
LOGGER = logging.getLogger("einvoice_app")

#Called from lambda_function.py
#Reading the config file from s3 bucket
def read_config_file_from_bucket(bucket_name, temp_path, default_config_path):
    # pylint: disable-msg=W0703
    # pylint: disable-msg=W0613
    '''
    Input  -
       params: bucket_name - The s3 bucket
       params: s3_object - s3 object to connect with boto3
       param: temp_path - The file path
       param: default_config_path - The configuration file path
    Output -  The config file is read from s3 bucket
    '''
    file_dict = {}
    try:
        s3_object = boto3.client('s3')
        s3_clientobj = s3_object.get_object(Bucket=bucket_name, Key=default_config_path)
        s3_clientdata = s3_clientobj['Body'].read().decode('utf-8')
        # s3_object.download_file(bucket_name, default_config_path, temp_path)
        # with open(temp_path, "r") as data:
        #     file_dict = json.load(data)
        file_dict = orjson.loads(s3_clientdata)
    except Exception as error:
        LOGGER.error("L1: EXCEPTION OCCURED %s", str(error), exc_info=True)
    return file_dict
