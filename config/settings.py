import yaml

class Settings:
    def __init__(self, env="dev"):
        with open("config/env.yaml") as f:
            data = yaml.safe_load(f)
        self.config = data[env]

settings = Settings()