import pytest, time
from core.driver_manager import DriverManager

# ======
# 全局 fixture
# ======
@pytest.fixture(scope="session")
def driver():
    options = DriverManager.ChromeOptions()
    options.page_load_strategy = "eager"
    driver = DriverManager.Chrome(options=options)
    driver.maximize_window()  # 浏览器窗口最大化
    yield driver
    driver.quit()

# =====================
# 全局慢速模式开关
# =====================
SLOW_MODE = True


def pause(seconds=1):
    if SLOW_MODE:
        time.sleep(seconds)