import boto3
from botocore.exceptions import ClientError
import base64
import logging
import hashlib
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

BUCKET_NAME = os.environ.get("BUCKETNAME")

def lambda_handler(event, context):
    logger.info(event)
    s3_client = boto3.client('s3')
    crate_name = event['pathParameters']['crate']
    version = event['pathParameters']['version']
    object_name = f"{crate_name[:2]}/{crate_name[2:4]}/{crate_name}-{version}.crate"
    # /ti/me/time-0.0.1.crate
    try:
        response = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': BUCKET_NAME,'Key': object_name}, ExpiresIn=3600)
    except ClientError as e:
        logging.error(e)
        return None

    return {
        "statusCode": 302,
        "headers": {
            "Location": response
        }
    }
