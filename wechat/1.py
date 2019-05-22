# -*- coding:utf-8 -*-          
# @Time     :2019/5/13 15:41    
# @Author   :LW                 
# @File     :1.py         

# query = ('情感', '健身', '茶', '杭州', '小姐', '种草', '美妆', '学姐', '佳人', '美丽', '姨', '打扮', '剁手', '丫头', '美容', '秘密', '洋气', '气质', '魅', '网红', '优雅', '精致', '纹身', 'tattoo', '故事', '连衣裙', '韩版', '美版')


import os
from xlutils.copy import copy
import xlrd as ExcelRead


def write_append(file_name):
    values = ["Ann", "woman", 22, "UK"]

    r_xls = ExcelRead.open_workbook(file_name)
    r_sheet = r_xls.sheet_by_index(0)   # 取第一个sheet
    # rows = r_sheet.nrows
    w_xls = copy(r_xls)
    sheet_write = w_xls.get_sheet(0)

    for i in range(0, len(values)):
        sheet_write.write(rows, i, values[i])

    w_xls.save(file_name + '.out' + os.path.splitext(file_name)[-1]);


if __name__ == "__main__":
    write_append("./test_append.xls")