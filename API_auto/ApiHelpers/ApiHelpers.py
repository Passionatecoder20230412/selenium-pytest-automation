import requests


class APIHelpers:

    def __init__(self, base_url, headers=None, timeout=10):
        self.base_url = base_url
        self.headers = headers
        self.timeout = timeout

    def get_api(self, end_point, params=None):
        url = self.base_url + end_point
        return requests.get(
            url,
            params=params,
            headers=self.headers,
            timeout=self.timeout
        )

    def post_api(self, end_point, json=None, params=None):
        url = self.base_url + end_point
        return requests.post(
            url,
            json=json,
            params=params,
            headers=self.headers,
            timeout=self.timeout
        )

    def put_api(self, end_point, json=None, params=None):
        url = self.base_url + end_point
        return requests.put(
            url,
            json=json,
            params=params,
            headers=self.headers,
            timeout=self.timeout
        )

    def patch_api(self, end_point, json=None, params=None):
        url = self.base_url + end_point
        return requests.patch(
            url,
            json=json,
            params=params,
            headers=self.headers,
            timeout=self.timeout
        )

    def delete_api(self, end_point, json=None, params=None):
        url = self.base_url + end_point
        return requests.delete(
            url,
            json=json,
            params=params,
            headers=self.headers,
            timeout=self.timeout
        )