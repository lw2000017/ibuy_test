# coding:utf-8

import unittest


class Test(unittest.TestCase):
    def setUp(self):
        print("hello")

    def tearDown(self):
        print("byebye")

    def test_01(self):
        print(2)


if __name__ == '__main__':
    unittest.main()
