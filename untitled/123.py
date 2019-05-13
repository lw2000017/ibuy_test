# coding:utf-8
import xlrd

data = xlrd.open_workbook('手机号.xlsx')
table = data.sheet_by_name('Sheet1')
nrows = table.nrows
# print(nrows)

for i in range(1, nrows):
    # print(i)
    beiyaoqingren = table.row_values(i)[0]
    yaoqingren = table.row_values(i)[1]
    print(type(beiyaoqingren))
    print(yaoqingren)