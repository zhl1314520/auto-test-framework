import os

# 跑所有用例
def run_all():
    os.system("pytest -v")

# 跑指定目录
def run_dir(dir):
    os.system("pytest " + dir + " -v")

# 跑指定文件
def run_file(file):
    os.system("pytest " + file + " -v")

# 跑指定用例
def run_case(file, name):
    os.system("pytest " + file + "::" + name + " -v")

if __name__ == "__main__":
    # run_case("tests/api/test_user.py", "test_login")

    # run_case("tests/api/test_user.py", "test_get_current_user_info")

    run_case("tests/api/test_user.py", "test_get_current_user_info")