import requests

class APIClient:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.session = requests.Session()
        if headers:
            self.session.headers.update(headers)

    def get(self, endpoint, params=None, **kwargs):
        return self.session.get(f"{self.base_url}{endpoint}", params=params, **kwargs)

    def post(self, endpoint, data=None, json=None, **kwargs):
        return self.session.post(f"{self.base_url}{endpoint}", data=data, json=json, **kwargs)

    def put(self, endpoint, data=None, **kwargs):
        return self.session.put(f"{self.base_url}{endpoint}", data=data, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.session.delete(f"{self.base_url}{endpoint}", **kwargs)