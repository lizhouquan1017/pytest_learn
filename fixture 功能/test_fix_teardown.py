# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/5 下午3:58
@Auth ： lizhouquan
@File ：test_fix_teardown.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import pytest


@pytest.fixture(scope="module")
def open_chrome():
    print("打开浏览器,并且打开百度首页")

    yield
    print("执行teardown!")
    print("最后关闭浏览器")


def test_s1(open_chrome):
    print("用例1：搜索python-1")


def test_s2(open_chrome):
    print("用例2：搜索python-2")


def test_s3(open_chrome):
    print("用例3：搜索python-3")


if __name__ == "__main__":
    pytest.main(["-s", "test_fix_teardown.py"])
