import base64
import logging
import hashlib

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info(event)
    with open('time-0.0.1.crate', 'rb') as g:
      raw_file = g.read()
      print(hashlib.sha256(raw_file).hexdigest())
    response = base64.b64encode(raw_file).decode('utf-8')
    return {
        "statusCode": 200,
        'body': response,
        'isBase64Encoded': True,
        "headers": {
            "Content-Type": "application/json",
            "Content-Encoding": "gzip"
        }
    }
