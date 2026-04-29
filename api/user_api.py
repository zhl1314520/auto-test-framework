from core.base_api import BaseAPI


class UserAPI(BaseAPI):

    def get_user(self, user_id):
        return self.get(f"/users/{user_id}")