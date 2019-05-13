# -*- coding:utf-8 -*-
# @Time     :2019/4/17 19:30
# @Author   :LW
# @File     :1.py

import yaml

fs = open("caps.yaml")

datas = yaml.load(fs)
print(datas)