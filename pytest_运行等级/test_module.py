# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/4 下午4:30
@Auth ： lizhouquan
@File ：test_module.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import pytest


def setup_module():
    print("setup_module：整个.py模块只执行一次")
    print("比如：所有用例开始前只打开一次浏览器")


def teardown_module():
    print("teardown_module：整个.py模块只执行一次")
    print("比如：所有用例结束只最后关闭浏览器")


def setup_function():
    print("setup_function：每个用例开始前都会执行")


def teardown_function():
    print("teardown_function：每个用例结束前都会执行")


def test_one():
    print("正在执行----test_one")


def test_two():
    print("正在执行----test_two")


class TestCase:

    def setup_class(self):
        print("setup_class：所有用例执行之前")

    def teardown_class(self):
        print("teardown_class：所有用例执行之前")

    def test_three(self):
        print("正在执行----test_three")

    def test_four(self):
        print("正在执行----test_four")


if __name__ == "__main__":
    pytest.main(["-s", "test_fixtclass.py"])
