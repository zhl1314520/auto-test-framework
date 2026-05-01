import yaml

class Settings:
    # 后端配置
    def __init__(self, env="dev"):
        with open("config/env.yaml", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        self.config = data[env]

settings = Settings()

class SettingsFrontend:
    # 前端配置
    def __init__(self, env="dev-vue"):
        with open("config/env.yaml", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        self.config = data[env]

settings_frontend = SettingsFrontend()