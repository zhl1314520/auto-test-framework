from pages.login_page import LoginPage
import pytest

""" 登录模块 """
@pytest.mark.parametrize("email, password, expected_success", [
    ("17201665342@163.com", "123456", True),
    ("17201665342@163.com", "123123", False),
    ("10293832823@163.com", "123456", False),
    ("", "123456", False),
    ("17201665342@163.com", "", False),
])
def test_login(driver, email, password, expected_success):
    page = LoginPage(driver)
    page.open()
    page.login(email, password)

    assert page.is_login_success() == expected_success