import pytest

""" 用户认证 """


@pytest.mark.parametrize("email,password,expected_status", [
    ("17201665342@163.com", "123456", 200),
    ("17263937422@163.com", "", 401),
    ("", "123456", 401),
])
def test_login(auth_api_with_token, email, password, expected_status):
    result = auth_api_with_token.login(email, password)
    assert result.status_code == expected_status


def test_get_current_user_info(auth_api_with_token, expected_status = 200):
    result = auth_api_with_token.get_current_user_info()
    assert result.status_code == expected_status