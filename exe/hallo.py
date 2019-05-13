# -*- coding:utf-8 -*-
# @Time     :2019/5/7 16:54    
# @Author   :LW                 
# @File     :hallo.py         

import time
import json
import xlwt
import xlrd
from xlutils.copy import copy


def new_excel(name, shname):
    """新建一个新的excel，若是种类相同，则用下面的追加写入excel"""
    # 新建一个excel
    workbook = xlwt.Workbook()
    # 新建一个sheet名
    sheet = workbook.add_sheet(f'{name}-{shname}')
    return sheet, workbook


def append_excel(name, shname):
    """追加写入excel,若是需要新建excel，则用上面的新建excel"""
    # 打开excel
    new_work = xlrd.open_workbook(path)
    workbook = copy(new_work)    # 相当于复制文件
    # 新建sheet名字，新建的名字不能和当前excel里的sheet名称重复
    sheet = workbook.add_sheet(f'{name}-{shname}')
    return sheet, workbook


def read_json():
    """读json文件"""
    # 打开json文件
    with open('a.json') as f:
        dict_json = json.load(f)     # 把json文件转换为字典格式
    return dict_json


def write_excel(row0, sheet, response, ziduan):
    """写入excel"""
    for j in range(len(row0)):
        sheet.write(0, j, row0[j])      # 写入第一行，标题
    zd = ziduan.split(' ')
    # print(zd)
    # print(len(zd))
    for line in range(len(response)):
        # title = response[line]['title']
        # price = response[line]['price']
        # vipPrice = response[line]['vipPrice']
        # salesVolume = response[line]['salesVolume']
        for i in range(len(zd)):
            sheet.write(line+1, i, response[line][zd[i]])


if __name__ == '__main__':
    num = 0
    sum = 0
    # 新建excel的名称
    excel_name = input("请输入excel文件名称：")
    # sheet 名称
    shname = input('请输入excel里sheet名称：')
    # excel路径，为了方便，我就放在了当前路径下
    path = f'{excel_name}.xls'
    # excel文件中，第一行的标题
    row0_str = input('请输入你所需要的标题名称（空格隔开）：')
    row0 = row0_str.split(' ')
    ziduan = input('请输入你需要的字段名（空格隔开）：')
    # # 读取文件，并获取返回结果
    # # 每次都要读取一次
    # dict_json = read_json()
    # # 提取想要的数据
    # response = dict_json

    while sum < 1:

        if num == 0:
            """第一次打开"""
            is_new = int(input("请确认是否为新建excel（0是1否）："))
            if is_new == 0:
                """新建excel"""
                # 读取文件，并获取返回结果
                # 每次都要读取一次
                dict_json = read_json()
                # 提取想要的数据
                response = dict_json
                new = new_excel(excel_name, shname)
                sheet = new[0]
                workbook = new[1]
                # 写入excel
                write_excel(row0, sheet, response, ziduan)
                workbook.save(path)
                print('写入完成\n')
            elif is_new == 1:
                """不是新建excel，可以拿之前的文件名"""
                shname = input('请输入excel里新sheet名称：')

                is_replace = int(input("是否需要重新修改标题名和所需字段（0是1否）："))
                if is_replace == 0:
                    """重新修改字段名和标题名"""
                    row0_str = input('请输入你所需要的标题名称（空格隔开）：')
                    row0 = row0_str.split(' ')

                    ziduan = input('请输入你需要的字段名（空格隔开）：')
                    # 读取文件，并获取返回结果
                    # 每次都要读取一次
                    dict_json = read_json()
                    # 提取想要的数据
                    response = dict_json
                    append = append_excel(excel_name, shname)
                    sheet = append[0]
                    workbook = append[1]
                    # 写入excel
                    write_excel(row0, sheet, response, ziduan)
                    workbook.save(path)
                    print('写入完成\n')

                elif is_replace == 1:

                    """不修改标题和字段，只是新增一个sheet"""
                    # 读取文件，并获取返回结果
                    # 每次都要读取一次
                    dict_json = read_json()
                    # 提取想要的数据
                    response = dict_json

                    ziduan = input('请输入你需要的字段名（空格隔开）：')
                    append = append_excel(excel_name, shname)
                    sheet = append[0]
                    workbook = append[1]
                    # 写入excel
                    write_excel(row0, sheet, response, ziduan)
                    workbook.save(path)
                    print('写入完成\n')


        else:
            is_replace = int(input("是否需要重新修改标题名和所需字段（0是1否）："))
            if is_replace == 0:
                """重新修改字段名和标题名"""
                row0_str = input('请输入你所需要的标题名称（空格隔开）：')
                row0 = row0_str.split(' ')

                ziduan = input('请输入你需要的字段名（空格隔开）：')
                is_sheet = int(input('是否需要新增sheet（0是1否）：'))
                if is_sheet == 0:
                    shname = input('请输入excel里新sheet名称：')
                    # 读取文件，并获取返回结果
                    # 每次都要读取一次
                    dict_json = read_json()
                    # 提取想要的数据
                    response = dict_json
                    append = append_excel(excel_name, shname)
                    sheet = append[0]
                    workbook = append[1]
                    # 写入excel
                    write_excel(row0, sheet, response, ziduan)
                    workbook.save(path)
                    print('写入完成\n')
                elif is_sheet == 1:
                    print('不新增sheet，会覆盖掉之前的数据')
                    dict_json = read_json()
                    # 提取想要的数据
                    response = dict_json
                    new = new_excel(excel_name, shname)
                    sheet = new[0]
                    workbook = new[1]
                    # 写入excel
                    write_excel(row0, sheet, response, ziduan)
                    workbook.save(path)
                    print('写入完成\n')

            elif is_replace == 1:
                """不修改标题和字段，只是新增一个sheet"""
                # 读取文件，并获取返回结果
                # 每次都要读取一次
                dict_json = read_json()
                # 提取想要的数据
                response = dict_json
                shname = input('请输入excel里新sheet名称：')
                append = append_excel(excel_name, shname)
                sheet = append[0]
                workbook = append[1]
                # 写入excel
                write_excel(row0, sheet, response, ziduan)
                workbook.save(path)
                print('写入完成\n')
        num += 1

        is_end = int(input("是否结束写入（0是1否）："))
        if is_end == 0:
            sum = 1
        elif is_end == 1:
            continue





















'''



        # excel文件中，第一行的标题
        row0_str = input('请输入你所需要的标题名称（空格隔开）：')
        row0 = row0_str.split(' ')

        is_new = int(input("请确认是否为新建excel（0是1否）："))
        if is_new == 0:
            """新建excel"""
            # 新建excel的名称
            excel_name = input("请输入excel文件名称：")
            # sheet 名称
            shname = input('请输入excel里sheet名称：')
            # excel路径，为了方便，我就放在了当前路径下
            path = f'{excel_name}.xls'
            # 读取文件，并获取返回结果
            dict_json = read_json()
            # 提取想要的数据
            response = dict_json

            new = new_excel(excel_name, shname)
            sheet = new[0]
            workbook = new[1]
            # 写入excel
            write_excel(row0, sheet, response)
            workbook.save(path)
            print('写入完成')
        elif is_new == 1:
            is_replace = int(input("是否需要重新修改标题名和所需字段（0是1否）："))
            if is_replace == 0:
                """重新修改字段名和标题名"""
                row0_str = input('请输入你所需要的标题名称（空格隔开）：')
                row0 = row0_str.split(' ')
            elif is_replace == 1:
                """不修改"""
                append = append_excel(excel_name, shname)
                sheet = append[0]
                workbook = append[1]
                # 写入excel
                write_excel(row0, sheet, response, ziduan)
                workbook.save(path)
                print('写入完成')







    # 新建excel的名称
    excel_name = input("请输入excel文件名称：")
    # sheet 名称
    shname = input('请输入excel里sheet名称：')
    # excel路径，为了方便，我就放在了当前路径下
    path = f'{excel_name}.xls'
    # excel文件中，第一行的标题
    # row0 = ['商品名称', '销售价格', '会员价格', '销售总量']
    row0_str = input('请输入你所需要的标题名称（空格隔开）：')
    row0 = row0_str.split(' ')
    # print(row0)
    # 读取文件，并获取返回结果
    dict_json = read_json()
    # 提取想要的数据
    response = dict_json

    is_new = input("请确认是否为新建excel（是或否）：")
    if is_new == '是':
        """新建一个新的excel，若是种类相同，则用下面的追加写入excel"""
        new = new_excel(excel_name, shname)
        sheet = new[0]
        workbook = new[1]
        # 写入excel
        write_excel(row0, sheet, response)
        workbook.save(path)
        print('写入完成')
    elif is_new == '否':
        """追加写入excel,若是需要新建excel，则用上面的新建excel"""
        append = append_excel(excel_name, shname)
        sheet = append[0]
        workbook = append[1]
        # 写入excel
        write_excel(row0, sheet, response)
        workbook.save(path)
        print('写入完成')
    time.sleep(2)'''
