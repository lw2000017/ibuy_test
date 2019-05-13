# coding:utf-8

import unittest


class Test(unittest.TestCase):
    def setUp(self):
        print("hallo!")

    def tearDown(self):
        print("bye!")

    def test_01(self):
        print(1)


if __name__ == '__main__':
    unittest.main()
