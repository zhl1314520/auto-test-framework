

""" 接口封装 """
import requests

class BaseAPI:
    def __init__(self):
        self.session = requests.Session()

    def get(self, url, **kwargs):
        return self.session.get(url, **kwargs)

    def post(self, url, **kwargs):
        return self.session.post(url, **kwargs)