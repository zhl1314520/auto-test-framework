import pytest
import json

""" 用户管理 """


@pytest.mark.parametrize("username, password, role, email, expected_status", [
    ("framework_user3", "123123", "developer", "13872631939@163.com", 200),
])
def test_create_user(user_api, username, password, role, email, expected_status):
    result = user_api.test_create_user(username, password, role, email)
    assert result.status_code == expected_status


@pytest.mark.parametrize("page, page_size, expected_status", [
    (1, 10, 200)
])
def test_user_list(user_api, page, page_size, expected_status):
    result = user_api.get_user_list()
    assert result.status_code == expected_status
    # print(result.json())
    # 按照 json 标准输出格式打印
    print(json.dumps(result.json(), indent=2))


@pytest.mark.parametrize("id, expected_status", [
    (11, 200)
])
def test_delete_user_by_id(user_api, id, expected_status):
    result = user_api.delete_user(id)
    assert result.status_code == expected_status


@pytest.mark.parametrize("id, email, role, expected_status", [
    (3, "17201665342@163.com", "tester", 200)   # 用户需要跟 token 匹配
])
def test_update_user_info(user_api, id, email, role, expected_status):
    result = user_api.update_user_info(id, email, role)
    assert result.status_code == expected_status

