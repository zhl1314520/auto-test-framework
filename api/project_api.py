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
        return self.delete(url)

    @allure.step("调用更新项目接口: {id}")
    def update_project_by_id(self, id, name, description):
        url = settings.config["base_url"] + "/projects/" + str(id)
        payload = {
            "name": name,
            "description": description
        }
        return self.put(url, json=payload)

    @allure.step("调用添加项目成员接口: {id}")
    def add_project_member(self, id, project_id, user_id, role):
        url = settings.config["base_url"] + "/projects/" + str(id) + "/members"
        payload = {
            "project_id": project_id,
            "user_id": user_id,
            "role": role
        }
        return self.post(url, json=payload)

    @allure.step("调用获取项目成员列表接口: {id}")
    def get_project_member_list(self, id):
        url = settings.config["base_url"] + "/projects/" + str(id) + "/members"
        return self.get(url)

    @allure.step("调用删除项目成员接口: {member_id}")
    def delete_project_member_by_member_id(self, member_id):
        url = settings.config["base_url"] + "/projects" + "/members/" + str(member_id)
        return self.delete(url)