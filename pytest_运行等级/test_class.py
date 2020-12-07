# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/4 下午4:18
@Auth ： lizhouquan
@File ：test_method.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import pytest


class TestCase:

    def setup_class(self):
        print("setup_class：所有用例执行之前")

    def teardown_class(self):
        print("teardown_class：所有用例执行之前")

    def test_one(self):
        print("正在执行----test_one")

    def test_two(self):
        print("正在执行----test_two")


if __name__ == "__main__":
    pytest.main(["-s", "test_class.py"])
