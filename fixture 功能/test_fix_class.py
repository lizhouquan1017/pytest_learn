# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/5 下午3:01
@Auth ： lizhouquan
@File ：test_fix_class.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import pytest


@pytest.fixture(scope="class")
def fixture_value():
    print('执行scope=class的pytest\n')
    value = 'testcase'
    return value


class TestClass:
    def test_1(self, fixture_value):
        """
        用例传入fixture值
        :param fixture_value:
        :return:
        """
        print("测试账号:%s" % fixture_value)
        assert fixture_value == "testcase"

    def test_2(self, fixture_value):
        """
        用例传入fixture的值
        :param first:
        :return:
        """
        print("测试账号:%s" % fixture_value)
        assert fixture_value == "testcase"


if __name__ == "__main__":
    pytest.main(["-s", "test_fix_class.py"])
