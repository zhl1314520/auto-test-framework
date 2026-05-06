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
