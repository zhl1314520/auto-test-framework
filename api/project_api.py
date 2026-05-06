import allure
from utils.get_token_util import get_token
from core.base_api import BaseAPI
from config.settings import settings


class ProjectAPI(BaseAPI):
    @allure.step("调用创建项目接口: {name}")
    def create_project(self, name, description):
        url = settings.config["base_url"] + "/projects"
        payload = {
            "name": name,
            "description": description
        }
        headers = {"Authorization": f"Bearer {get_token()}"}
        return self.post(url, json=payload, headers=headers)

    @allure.step("调用获取项目列表接口: ")
    def get_project_list(self, page, page_size):
        url = settings.config["base_url"] + "/projects"
        headers = {"Authorization": f"Bearer {get_token()}"}
        return self.get(url, params={"page": page, "page_size": page_size}, headers=headers)

    @allure.step("调用删除项目接口: {id}")
    def delete_project_by_id(self, id):
        url = settings.config["base_url"] + "/projects/" + str(id)
        # headers = {"Authorization": f"Bearer {get_token()}"}
        return self.delete(url)