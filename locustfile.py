from locust import HttpUser, task
from authorizer import authorize
import config as conf
import json

# For content type=text/csv use below line
# PAYLOAD = '0.234234,0.234345,0.5634,-0.23535'

# For content type=application/json use similar to below 2 lines
PAYLOAD = '<html lang="en" dir="ltr"><head> <title>Login in your account</title> </head> </html>'


class WebsiteUser(HttpUser):
    min_wait = 1
    max_wait = 5  # time in ms

    @task
    def test_post(self):
        """
        Load Test SageMaker Endpoint (POST request)
        """
        headers = authorize(PAYLOAD)

        print("HEAD:", headers)

        self.client.post(conf.SAGEMAKER_ENDPOINT_URL, data=PAYLOAD, headers=headers, name='Post Request')
