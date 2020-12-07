# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/5 下午3:44
@Auth ： lizhouquan
@File ：test_fix_session_1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import pytest


def test_2(login):
    """
    传入fixture值
    :param first:
    :return:
    """
    print("测试账号：%s" % login)
    assert login == "test_session"


if __name__ == "__main__":
    pytest.main(["-s", "test_fix_session_2.py"])


#  pytest -s test_fix_session_1.py test_fix_session_2.py
