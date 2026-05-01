from core.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.settings import settings_frontend
from selenium.webdriver.support.ui import Select

class TestcasePage(BasePage):
    url = settings_frontend.config["base_url"] + "/dashboard/testcases"

    select_list = (By.CLASS_NAME, "filter-select")

    def open(self):
        self.driver.get(self.url)

    def get_select_options_count(self, select_index=0):
        """获取指定下拉框的选项数量"""
        selects = self.finds(self.select_list)
        select = Select(selects[select_index])
        return len(select.options)

    def select_by_index(self, select_index, option_index):
        """指定下拉框选择指定选项"""
        selects = self.finds(self.select_list)
        Select(selects[select_index]).select_by_index(option_index)

    def get_selected_text(self, select_index=0):
        """获取指定下拉框当前选中的文本"""
        selects = self.finds(self.select_list)
        return Select(selects[select_index]).first_selected_option.text