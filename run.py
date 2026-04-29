import os

os.system("pytest -v --alluredir=allure-results")
os.system("allure generate allure-results -o allure-report --clean")
os.system("allure open allure-report")