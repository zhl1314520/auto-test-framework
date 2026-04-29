from core.base_page import BasePage

class LoginPage(BasePage):

    def login(self, email, password):
        self.input_username(email)
        self.input_password(password)
        self.click_login()