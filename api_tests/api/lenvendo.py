import requests
from urllib.parse import urljoin


class LevendoAPIEndpoints:
    JS_TEST_TASK = "api/js-test-task"


class LenvendoAPI():
    def __init__(self, base_url):
        self.base_url = base_url

    def get_js_test_task(self, params=None):
        url = urljoin(self.base_url, LevendoAPIEndpoints.JS_TEST_TASK)
        resp = requests.get(url, params=params)
        return resp
