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
    sheet = workbook.add_sheet(f'{excel_name}-{shname}')
    return sheet, workbook


def append_excel(excel_name, shname):
    """追加写入excel,若是需要新建excel，则用上面的新建excel"""
    # 打开excel
    new_work = xlrd.open_workbook(path)
    workbook = copy(new_work)    # 相当于复制文件
    # 新建sheet名字，新建的名字不能和当前excel里的sheet名称重复
    sheet = workbook.add_sheet(f'{excel_name}-{shname}')
    return sheet, workbook


def read_json():
    """读json文件"""
    # 打开json文件
    with open('a.json', encoding='utf-8') as f:
        dict_json = json.load(f)     # 把json文件转换为字典格式
    return dict_json


def write_excel(row0, sheet, response):
    """写入excel"""
    for j in range(len(row0)):
        sheet.write(0, j, row0[j])      # 写入第一行，标题
    # ziduan = input('请输入你需要的字段名（空格隔开）：')
    # zd = ziduan.split(' ')
    # print(zd)
    # print(len(zd))
    for line in range(len(response)):
        name = response[line]['title']
        price = response[line]['price']
        vipPrice = response[line]['vipPrice']
        salesVolume = response[line]['salesVolume']
        # volume = response[line]['volume']
        # for i in range(len(zd)):
        sheet.write(line+1, 0, name)
        sheet.write(line+1, 1, price)
        sheet.write(line+1, 2, vipPrice)
        sheet.write(line+1, 3, salesVolume)
        # sheet.write(line+1, 4, volume)




if __name__ == '__main__':
    # 新建excel的名称
    # excel_name = input("请输入excel文件名称：")
    excel_name = '环球捕手-夏日必备'
    # sheet 名称
    # shname = input('请输入excel里sheet名称：')
    shname = '清洁洗晒之清洁工具'
    # excel路径，为了方便，我就放在了当前路径下
    path = f'{excel_name}.xls'
    # excel文件中，第一行的标题
    row0 = ['商品名称', '销售价格', '会员价格',  '最近销售量']
    # row0_str = input('请输入你所需要的标题名称（空格隔开）：')
    # row0 = row0_str.split(' ')
    # print(row0)
    # 读取文件，并获取返回结果
    dict_json = read_json()
    # 提取想要的数据
    response = dict_json['data']['categoryItemResultVOS']
    # 0 新建，1追加
    is_new = 1

    """
    new_work = xlrd.open_workbook(path)
    workbook = copy(new_work)    # 相当于复制文件
    # 新建sheet名字，新建的名字不能和当前excel里的sheet名称重复
    sheet = workbook.add_sheet(f'{excel_name}-{shname}')

    with open(f'{excel_name}.txt', 'r') as f:
    #     for line in range(len(response)):
    #         title = response[line]['title']
    #         price = response[line]['price']
    #         vipPrice = response[line]['vipPrice']
    #         f.write(f'{title}，。{price}，。{vipPrice}\n')
    #     f.close()

        lines = f.readlines()
        for line in range(len(lines)):
            title = lines[line].split('，。')[0]
            price = lines[line].split('，。')[1]
            vipPrice = lines[line].split('，。')[2]
            sheet.write(line+1, 0, title)
            sheet.write(line+1, 1, price)
            sheet.write(line+1, 2, vipPrice)
    workbook.save(path)"""




    if is_new == 0:
        '''新建一个新的excel，若是种类相同，则用下面的追加写入excel'''
        new = new_excel(excel_name, shname)
        sheet = new[0]
        workbook = new[1]
        # 写入excel
        write_excel(row0, sheet, response)
        workbook.save(path)
        print('写入完成')
    elif is_new == 1:
        '''追加写入excel,若是需要新建excel，则用上面的新建excel'''
        append = append_excel(excel_name, shname)
        sheet = append[0]
        workbook = append[1]
        # 写入excel
        write_excel(row0, sheet, response)
        workbook.save(path)
        print('写入完成')
    # time.sleep(2)"""
