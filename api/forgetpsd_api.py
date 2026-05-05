import allure
from core.base_api import BaseAPI
from config.settings import settings


class ForgetPsdAPI(BaseAPI):
    @allure.step("调用忘记密码接口: {email}")
    def send_verifycode(self, email):
        url = settings.config["base_url"] + "/password-reset/send-code"
        return self.post(url, params={"email": email})  # 后端使用的是查询参数

    @allure.step("调用重置密码接口: {email}")
    def reset_password(self, email, code):
        url = settings.config["base_url"] + "/password-reset/verify-code"
        return self.post(url, params={"email": email, "code": code})