from api.user_api import UserAPI

def test_get_user():
    api = UserAPI()
    res = api.get_user(1)
    assert res.status_code == 200