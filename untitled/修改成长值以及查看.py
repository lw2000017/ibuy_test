import pymysql
import requests
import xlrd




if __name__ == '__main__':

    data = xlrd.open_workbook('手机号.xlsx')  # 打开在该脚本路径下的excel文件，如果需要其他路径，把其他路径复制上即可
    table = data.sheet_by_name('Sheet5')  # 获取某个sheet内容
    rows = table.nrows  # 获取总行数

    db = pymysql.connect('ibuyibuy.mysql.rds.aliyuncs.com', 'ibuy_test', 'ibuy9735!$)*', 'ibuy_test_v2')

    cursor = db.cursor()
    # invitee_list = []
    for i in range(1, rows):

        invitee = int(table.row_values(i)[0])
        # 修改密码  第一次需要，之后就不需要了
        sql_pwd = "UPDATE amc_user SET `password` = '14e1b600b1fd579f47433b88e8d85291' WHERE phone = '{}'".format(invitee)
        # 修改成长值
        sql_grow = "UPDATE amc_user_account SET growth_value = 990 WHERE phone = '{}'".format(invitee)

        try:
            cursor.execute(sql_pwd)
            # cursor.execute(sql_grow)
        except Exception as e:
            db.rollback()
            print('处理失败---{}'.format(invitee))
        else:
            db.commit()
            print('处理成功---{}'.format(invitee))

    cursor.close()
    db.close()

    # # 最终
    # phone_list = []
    #
    # for i in range(len(invitee_list)):
    #     phone_list.append(invitee_list[i])
