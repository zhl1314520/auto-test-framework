import requests
from config.settings import settings

# 登录获取 token
def get_token():
    login_response = requests.post(
        settings.config["base_url"] + "/auth/login",
        json={
            "email": "17201665342@163.com",
            "password": "123456"
        })
    token = login_response.json()["token"]
    return token

