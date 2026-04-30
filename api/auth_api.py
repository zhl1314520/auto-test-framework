import allure
from core.base_api import BaseAPI
from config.settings import settings
from utils.get_token_util import get_token

class AuthAPI(BaseAPI):

    @allure.step("调用登录接口: {email}")
    def login(self, email, password):
        url = settings.config["base_url"] + "/auth/login"

        payload = {
            "email": email,
            "password": password
        }

        return self.post(url, json=payload)

    @allure.step("调用获取用户信息接口: ")
    def get_current_user_info(self):
        url = settings.config["base_url"] + "/auth/me"
        headers = {"Authorization": f"Bearer {get_token()}"}
        return self.get(url, headers=headers)