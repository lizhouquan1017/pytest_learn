# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/5 下午3:11
@Auth ： lizhouquan
@File ：test_fix_module.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import pytest


@pytest.fixture(scope="module")
def fixture_module_value():
    print("\nscope为module级别当前.py模块只运行一次\n")
    value = 'test_module'
    return value


def test_1(fixture_module_value):
    """
    传入fixture的值
    :param fixture_module_value:
    :return:
    """
    print('类外面的test用例: %s' % fixture_module_value)
    assert fixture_module_value == "test_module"


class TestCase:
    def test_2(self, fixture_module_value):
        """
        传入fixture的值
        :param fixture_module_value:
        :return:
        """
        print("类里面的测试用例: %s" % fixture_module_value)
        assert fixture_module_value == "test_module"


if __name__ == "__main__":
    pytest.main(["-s", "test_fix_module.py"])
