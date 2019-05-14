# -*- coding:utf-8 -*-
# @Time     :2019/5/7 16:54    
# @Author   :LW                 
# @File     :hallo.py         

import time
import json
import xlwt
import xlrd
from xlutils.copy import copy


def new_excel(excel_name, shname):
    """新建一个新的excel，若是种类相同，则用下面的追加写入excel"""
    # 新建一个excel
    workbook = xlwt.Workbook()
    # 新建一个sheet名
    sheet = workbook.add_sheet(f'{shname}')
    return sheet, workbook


def append_excel(excel_name, shname):
    """追加写入excel,若是需要新建excel，则用上面的新建excel"""
    # 打开excel
    new_work = xlrd.open_workbook(path)
    workbook = copy(new_work)    # 相当于复制文件
    # 新建sheet名字，新建的名字不能和当前excel里的sheet名称重复
    sheet = workbook.add_sheet(f'{shname}')
    return sheet, workbook


def read_json(names):
    """读json文件"""
    # 打开json文件

    with open(f'{names}.json', 'r', encoding='utf-8') as f_read:
        content = f_read.readlines()
        # print(content)
        # print(len(content))

    with open(f'{names}.json', 'w', encoding='utf-8') as f:
        for a in content:
            new_a = a.replace('}][{', '},{')
            f.write(new_a)
        f.close()

    with open(f'{names}.json', encoding='utf-8') as f:
        dict_json = json.load(f)     # 把json文件转换为字典格式
        f.close()
    return dict_json


def write_excel(row0, sheet, response):
    """写入excel"""
    for j in range(len(row0)):
        sheet.write(0, j, row0[j])      # 写入第一行，标题

    for line in range(len(response)):
        name = response[line]['itemName']
        price = response[line]['itemPrice']
        vipPrice = response[line]['itemVipPrice']
        # originalPrice = response[line]['originalPrice']
        # volume = response[line]['volume']
        # for i in range(len(zd)):
        sheet.write(line+1, 0, name)
        sheet.write(line+1, 1, price)
        sheet.write(line+1, 2, vipPrice)
        # sheet.write(line+1, 3, originalPrice)
        # sheet.write(line+1, 4, volume)


if __name__ == '__main__':
    # 新建excel的名称
    # excel_name = input("请输入excel文件名称：")
    excel_name = '云集-宠物生活'
    # sheet 名称
    # shname = input('请输入excel里sheet名称：')
    name = []

    for line in range(len(name)):
        shname = '{}'.format(name[line])
        # excel路径，为了方便，我就放在了当前路径下
        path = f'{excel_name}.xls'
        # excel文件中，第一行的标题
        row0 = ['商品名称', '特价', '原价']
        # 读取文件，并获取返回结果
        dict_json = read_json(names=name[line])
        # 提取想要的数据
        response = dict_json
        # 0 新建，1追加
        if line == 0:
            is_new = 0
            '''新建一个新的excel，若是种类相同，则用下面的追加写入excel'''
            new = new_excel(excel_name, shname)
            sheet = new[0]
            workbook = new[1]
            # 写入excel
            write_excel(row0, sheet, response)
            workbook.save(path)
            print('写入完成')
        elif line != 0:
            is_new = 1
            '''追加写入excel,若是需要新建excel，则用上面的新建excel'''
            append = append_excel(excel_name, shname)
            sheet = append[0]
            workbook = append[1]
            # 写入excel
            write_excel(row0, sheet, response)
            workbook.save(path)
            print('写入完成')
