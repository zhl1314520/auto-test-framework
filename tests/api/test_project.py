import pytest
import json

""" 项目管理 """

@pytest.mark.parametrize("name, description, expected_status", [
    ("5.6.1测试项目", "仅供测试使用", 200),
])
def test_create_project(project_api, name, description, expected_status):
    result = project_api.create_project(name, description)
    assert result.status_code == expected_status


@pytest.mark.parametrize("page, page_size, expected_status", [
    (1, 10, 200),
])
def test_get_project_list(project_api, page, page_size, expected_status):
    result = project_api.get_project_list(page, page_size)
    assert result.status_code == expected_status
    print(json.dumps(result.json(), indent=2))


@pytest.mark.parametrize("id, expected_status", [
    (33, 200),
])
def test_delete_project_by_id(project_api, id, expected_status):
    result = project_api.delete_project_by_id(id)
    assert result.status_code == expected_status


@pytest.mark.parametrize("id, name, description, expected_status", [
    (32, "5.6修改", "供接口测试使用", 200),
])
def test_update_project_by_id(project_api, id, name, description, expected_status):
    result = project_api.update_project_by_id(id, name, description)
    assert result.status_code == expected_status


@pytest.mark.parametrize("id, project_id, user_id, role, expected_status", [
    (32, 32, 4, "developer", 200),   # 项目32 + user_id=4
    (30, 30, 4, "developer", 200),   # 项目30 + user_id=4
    (28, 28, 4, "developer", 200),   # 项目28 + user_id=4
])
def test_add_project_member(project_api, id, project_id, user_id, role, expected_status):
    result = project_api.add_project_member(id, project_id, user_id, role)
    assert result.status_code == expected_status


@pytest.mark.parametrize("id, expected_status", [
    (32, 200)
])
def test_get_project_member_list(project_api, id, expected_status):
    result = project_api.get_project_member_list(id)
    assert result.status_code == expected_status
    print(json.dumps(result.json(), indent=2))


@pytest.mark.parametrize("member_id, expected_status", [
    (2, 200)
])
def test_delete_project_member_by_member_id(project_api, member_id, expected_status):
    result = project_api.delete_project_member_by_member_id(member_id)
    assert result.status_code == expected_status
