import allure
from core.base_api import BaseAPI
from config.settings import settings
from utils.get_token_util import get_token


class UserAPI(BaseAPI):
    @allure.step("调用创建用户接口: {username}")
    def test_create_user(self, username, password, role, email):
        url = settings.config["base_url"] + "/users"

        payload = {
            "username": username,
            "password": password,
            "role": role,
            "email": email
        }

        return self.post(url, json=payload)



    @allure.step("调用获取用户信息列表: ")
    def get_user_list(self):
        url = settings.config["base_url"] + "/users"
        return self.get(url)


    @allure.step("调用删除用户接口: {id}")
    def delete_user(self, id):
        url = settings.config["base_url"] + "/users/" + str(id) # 强转
        return self.delete(url)


    @allure.step("调用更新用户接口: {id}")
    def update_user_info(self, id, email, role):
        url = settings.config["base_url"] + "/users/" + str(id)
        payload = {
            "email": email,
            "role": role
        }
        headers = {"Authorization": f"Bearer {get_token()}"}
        return self.put(url, json=payload, headers=headers)


    @allure.step("调用获取用户详细信息: {id}")
    def get_user_details(self, id):
        url = settings.config["base_url"] + "/users/" + str(id)
        headers = {"Authorization": f"Bearer {get_token()}"}
        return self.get(url, headers=headers)


    @allure.step("调用修改用户密码接口: {id}")
    def change_user_password(self, id, old_password, new_password):
        url = settings.config["base_url"] + "/users/" + str(id) + "/password"
        payload = {
            "old_password": old_password,
            "new_password": new_password
        }
        headers = {"Authorization": f"Bearer {get_token()}"}
        return self.put(url, json=payload, headers=headers)
