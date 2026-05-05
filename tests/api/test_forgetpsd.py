import pytest
import json

""" 忘记密码 """

@pytest.mark.parametrize("email, expected_status", [
    ("17201665342@163.com", 200),
])
def test_send_verifycode(forget_password_api, email, expected_status):
    result = forget_password_api.send_verifycode(email)
    assert result.status_code == expected_status


@pytest.mark.parametrize("email, code, expected_status", [
    ("17201665342@163.com", "979284", 200),
])
def test_reset_password(forget_password_api, email, code, expected_status):
    result = forget_password_api.reset_password(email, code)
    assert result.status_code == expected_status