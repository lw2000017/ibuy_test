# -*- coding:utf-8 -*-          
# @Time     :2019/5/14 20:48    
# @Author   :LW                 
# @File     :环球捕手.py         

import json
import xlwt
import xlrd
from xlutils.copy import copy

with open('b.json', 'r', encoding='utf-8') as f:
    # dict = f.readline()
    dict_json = json.load(f)
    f.close()


excel_name = '环球捕手-滋补保健'
shname = '计生情趣'
path = '环球捕手-滋补保健.xls'

# 新建一个excel
# workbook = xlwt.Workbook()
# # 新建一个sheet名
# sheet = workbook.add_sheet(f'{shname}')


# 打开excel
new_work = xlrd.open_workbook(path)
workbook = copy(new_work)  # 相当于复制文件
# 新建sheet名字，新建的名字不能和当前excel里的sheet名称重复
sheet = workbook.add_sheet(f'{shname}')


response_dict = dict_json['data']['categoryItemResultVOS']
print(response_dict)
row0 = ['商品标题', '商品价格', '会员价格', '最近销售量']


for j in range(len(row0)):
    sheet.write(0, j, row0[j])

for line in range(len(response_dict)):
    name = response_dict[line]['title']
    price = response_dict[line]['price']
    vipPrice = response_dict[line]['vipPrice']
    salesVolume = response_dict[line]['salesVolume']
    sheet.write(line + 1, 0, name)
    sheet.write(line + 1, 1, price)
    sheet.write(line + 1, 2, vipPrice)
    sheet.write(line + 1, 3, salesVolume)

workbook.save(path)
