# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/5 下午4:18
@Auth ： lizhouquan
@File ：test_fix_request.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import pytest

# 测试账号数据
test_user_data = ["admin1", "admin2"]


@pytest.fixture(scope="module")
def login(request):
    user = request.param
    if user:
        return True
    else:
        return False


@pytest.mark.parametrize("login", test_user_data, indirect=True)
def test_login(login):
    """
    测试登录
    :param login:
    :return:
    """
    a = login
    print("login的返回值: %s" % a)
    assert a


if __name__ == "__main__":
    pytest.main(["-s", "test_fix_request"])
