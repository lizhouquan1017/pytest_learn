# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/4 下午4:18
@Auth ： lizhouquan
@File ：test_method.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import pytest


def setup_function():
    print("setup_function：每个用例开始前都会执行")


def teardown_function():
    print("teardown_function：每个用例结束后都会执行")


def test_one():
    print('第一个用例')


def test_two():
    print('第二个用例')


if __name__ == '__main__':
    pytest.main(['-s', 'test_method.py'])

