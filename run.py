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
    os.system("pytest " + file + "::" + name + " -v" + " -s")

if __name__ == "__main__":
    """ API """
    # run_case("tests/api/test_auth.py", "test_login")

    # run_case("tests/api/test_auth.py", "test_get_current_user_info")

    # run_case("tests/api/test_user.py", "test_create_user")

    # run_case("tests/api/test_user.py", "test_user_list")

    # run_case("tests/api/test_user.py", "test_delete_user_by_id")

    # run_case("tests/api/test_user.py", "test_update_user_info")

    # run_case("tests/api/test_user.py", "test_get_user_detail")

    # run_case("tests/api/test_user.py", "test_change_user_password")

    # run_case("tests/api/test_forgetpsd.py", "test_send_verifycode")

    # run_case("tests/api/test_forgetpsd.py", "test_reset_password")

    # run_case("tests/api/test_project.py", "test_create_project")

    # run_case("tests/api/test_project.py", "test_get_project_list")

    # run_case("tests/api/test_project.py", "test_delete_project_by_id")

    # run_case("tests/api/test_project.py", "test_update_project_by_id")

    # run_case("tests/api/test_project.py", "test_add_project_member")

    # run_case("tests/api/test_project.py", "test_get_project_member_list")

    run_case("tests/api/test_project.py", "test_delete_project_member_by_member_id")


    """ UI """
    # run_case("tests/ui/test_login.py", "test_login")

    # run_case("tests/ui/test_project.py", "test_project_input")

    # run_case("tests/ui/test_project.py", "test_project_scroll")

    # run_case("tests/ui/test_testcase.py", "test_select_list")