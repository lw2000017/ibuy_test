# coding:utf-8
import unittest
import HTMLTestRunner


def all_case():
    # 获取所有的测试用例
    case_dir = 'C:\/Users/please call me/PycharmProjects/项目搭建/case/'
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,
                                                   pattern="test*.py",
                                                   top_level_dir=None)

    for test_suite in discover:
        for test_case in test_suite:
            testcase.addTest(test_case)
        # print(testcase)
        return testcase


if __name__ == '__main__':
    report_path = 'C:\/Users/please call me/PycharmProjects/项目搭建/report/result.html'

    fp = open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="这是自动化报告",
                                           description="用例执行情况：")
    runner.run(all_case())
    fp.close()

