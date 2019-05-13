# coding:utf-8

import pytest

@pytest.fixture()
def login():
    print('输入账号，密码先登录')

def test_01(login):
    print('用例1，登录')


def test_02():
    print('用例2，不登录')

def test_03(login):
    print('用例3，登录后')


if __name__ == '__main__':
    pytest.main(['-s', 'test_one.py'])