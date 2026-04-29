from pages.login_page import LoginPage

def test_login(driver):
    page = LoginPage(driver)
    page.login("17201665342@163.com", "123456")
    assert "dashboard" in driver.current_url