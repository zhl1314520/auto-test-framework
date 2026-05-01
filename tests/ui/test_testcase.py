from pages.testcase_page import TestcasePage
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import pause, general_login

""" 用例模块 """
# 下拉列表
def test_select_list(driver, general_login):
    page = TestcasePage(driver)

    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
    page.open()
    options = page.get_select_options_count(0)
    for i in range(options):
        page.select_by_index(0, i)
        selected = page.get_selected_text(0)
        assert selected is not None
        pause(1)