from core.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.settings import settings_frontend


class LoginPage(BasePage):
    url = settings_frontend.config["base_url"] + "/login"

    email_input = (By.ID, "email")
    password_input = (By.ID, "password")
    submit_btn = (By.CLASS_NAME, "submit-button")

    def open(self):
        self.driver.get(self.url)

    def login(self, email, password):
        self.input(self.email_input, email)
        self.input(self.password_input, password)
        self.click(self.submit_btn)

    def is_login_success(self):
        # 页面跳转延迟，添加显示等待
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_contains("dashboard"))
        return "dashboard" in self.driver.current_url