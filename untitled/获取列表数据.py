import xlrd

data = xlrd.open_workbook('手机号.xlsx')  # 打开在该脚本路径下的excel文件，如果需要其他路径，把其他路径复制上即可
table = data.sheet_by_name('Sheet5')  # 获取某个sheet内容
rows = table.nrows  # 获取总行数
invitee_list = []

# print(rows)
# invitee_list = []
for i in range(1, rows):
    invitee = int(table.row_values(i)[0])  # 需要分享的人的手机号
    # print(invitee)
    invitee_list.append(str(invitee))

print(invitee_list)
