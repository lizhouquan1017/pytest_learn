# coding:utf-8
import pytest


@pytest.fixture(scope="session")
def login():
    print("scope为session级别多个.py模块只运行一次")
    return 'test_session'
