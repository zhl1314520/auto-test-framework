import pytest, time
from core.driver_manager import DriverManager
from api.auth_api import AuthAPI
from utils.get_token_util import get_token

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

# =====================
# 管理 token
# =====================
@pytest.fixture(scope="session")
def auth_token():
    """全局登录 token，整个测试会话只获取一次"""
    return get_token()


# 登录接口（带有 token）
@pytest.fixture
def auth_api_with_token(auth_token):
    """带 token 的 auth_api"""
    api = AuthAPI()
    api.token = auth_token  # 将 token 绑定到实例
    return api