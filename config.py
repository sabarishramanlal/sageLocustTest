HOST = 'runtime.sagemaker.us-east-1.amazonaws.com'
REGION = 'us-east-1'
# replace the url below with the sagemaker endpoint you are load testing
SAGEMAKER_ENDPOINT_URL = 'https://runtime.sagemaker.us-east-1.amazonaws.com/endpoints/py-sage-train-ursula-rf-2021-07-01-18-28-37-633/invocations'
ACCESS_KEY = 'AKIA4MUYUCLGVEOBMS74'
SECRET_KEY = 'wJ0IJU+SsvwXQ6GllbMAYJfyLjN9eFAXcDsEeB8I'
# replace the context type below as per your requirements
CONTENT_TYPE = 'text/csv'
# CONTENT_TYPE = 'application/json'
METHOD = 'POST'
SERVICE = 'sagemaker'
SIGNED_HEADERS = 'content-type;host;x-amz-date'
CANONICAL_QUERY_STRING = ''
ALGORITHM = 'AWS4-HMAC-SHA256'
