from core.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.settings import settings_frontend
import time


class ProjectPage(BasePage):
    url = settings_frontend.config["base_url"] + "/dashboard/projects"

    project_name_input = (By.CLASS_NAME, "search-input")

    def open(self):
        self.driver.get(self.url)

    def input_project_name(self, input_project_name):
        self.input(self.project_name_input, input_project_name)

    def is_search_project_success(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "projects-grid"))
            )
            return True
        except:
            return False

    def scroll_page(self, step, delay):
        """
            匀速慢慢滚动到页面底部
            :param step: 每次滚动的距离（像素），越小越慢
            :param delay: 每次滚动后的停顿时间（秒），越大越慢
            """
        # 获取当前滚动位置
        last_height = self.driver.execute_script("return window.pageYOffset;")

        while True:
            # 滚动一小段距离
            self.driver.execute_script(f"window.scrollBy(0, {step});")

            # 停顿一下，形成匀速效果
            time.sleep(delay)

            # 获取新的滚动位置
            new_height = self.driver.execute_script("return window.pageYOffset;")

            # 判断是否到达底部（当前位置和最新位置相同）
            if new_height == last_height:
                break
            last_height = new_height

        return last_height

    # 判断是否到达页面底部
    def is_reach_bottom(self, tolerance=5):
        # 获取视口高度（浏览器可见区域的高度）
        viewport_height = self.driver.execute_script("return window.innerHeight;")
        # 获取当前滚动位置（视口顶部到页面顶部的距离）
        scroll_position = self.driver.execute_script("return window.pageYOffset;")
        total_height = self.driver.execute_script("return document.body.scrollHeight;")

        # 添加容差值，允许几个像素的误差
        return scroll_position + viewport_height + tolerance >= total_height