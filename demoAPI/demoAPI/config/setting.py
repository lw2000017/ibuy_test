# -*- coding:utf-8 -*-          
# __Time__     :2019/5/21 15:27    
# __Author__   :LW                         


import os
import sys
# 基础文件路径 /demoAPI/demoAPI
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# 添加自己的搜索目录，把此目录放在环境变量中
sys.path.append(BASE_DIR)


# 配置文件
TEST_CONFIG = os.path.join(BASE_DIR, 'database', 'config.ini')
# 测试用例模板文件
SOURCE_FILE = os.path.join(BASE_DIR, 'database', )
# excel测试用例结果文件
TARGET_FILE = os.path.join(BASE_DIR, '')
# 测试用例报告
TEST_REPORT = os.path.join(BASE_DIR, 'report')
# 测试用例程序文件
TEST_CASE = os.path.join(BASE_DIR, 'testcase')
