# coding:utf-8
import requests
import hashlib
import xlrd
import pymysql


# 发送验证码
def Sms_url(url, headers):
    sms_body = {"data": {"phone": '{}'.format(invitee), "code_type": "SMS_LOGIN"}}
    requests.packages.urllib3.disable_warnings()  # 屏蔽https警告
    response = requests.post(url=url, json=sms_body, headers=headers, verify=False)
    # print(response.text)
    globals()['code'] = response.json()['data']['code']  # 获取 code
    globals()['biz'] = response.json()['data']['biz']  # 获取biz


# 填写邀请码，注册
def Sign_url(url, headers, sign_text):
    sign_body = {
        "data": {"phone": '{}'.format(invitee),
                 "code": str(globals()['code']),
                 "biz": str(globals()['biz']),
                 "sign": '{}'.format(sign_text),
                 "invite": '{}'.format(inviter)
                 }
    }
    requests.packages.urllib3.disable_warnings()  # 屏蔽https警告
    response = requests.post(url=url, json=sign_body, headers=headers, verify=False)
    if 'SUCCESS' in response.json()['msg']:
        print('{} 账号创建成功。'.format(invitee) + ' 他的上级是 {}'.format(inviter))
    else:
        print('%s 账号的错误细信息： ' % invitee + response.text)


# 修改密码
def Password_change(invitee):
    # 连接数据库
    db = pymysql.connect('ibuyibuy.mysql.rds.aliyuncs.com', 'ibuy_test', 'ibuy9735!$)*', 'ibuy_test_v2')
    # 创建一个游标对象
    cursor = db.cursor()
    # 更新语句
    sql = "UPDATE amc_user SET `password` = '14e1b600b1fd579f47433b88e8d85291' WHERE phone = '{}'".format(invitee)
    try:
        # 执行语句
        cursor.execute(sql)
        # 提交执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    db.close()




if __name__ == '__main__':
    sms_url = 'https://apptest.ibuycoinhd.com/site/sms'  # 发送验证码
    # login_url = 'https://apptest.ibuycoinhd.com/v22/site/login'  # 验证码登录
    sign_url = 'https://apptest.ibuycoinhd.com/v22/site/sign'  # 填写邀请人

    # 所有接口的请求头
    headers = {
        'Content-Type': 'application/json;charset=utf-8'
    }
    globals()['code'] = None
    globals()['biz'] = None
    globals()['access_token'] = None
    data = xlrd.open_workbook('手机号.xlsx')  # 打开在该脚本路径下的excel文件，如果需要其他路径，把其他路径复制上即可
    table = data.sheet_by_name('Sheet3')  # 获取某个sheet内容
    rows = table.nrows  # 获取总行数
    invitee_list = []
    for i in range(1, rows):

        invitee = int(table.row_values(i)[0])  # 被邀请人手机号
        inviter = int(table.row_values(i)[1])  # 邀请人手机号

        invitee_list.append(invitee)

        # 发送验证码
        Sms_url(url=sms_url, headers=headers)

        sign_text = 'APP_SIGN' + "{}".format(invitee) + str(globals()['code'])
        for i in range(2):
            m = hashlib.md5()
            m.update(b'%s' % sign_text.encode())
            sign_result = m.hexdigest()
            sign_text = sign_result
        # 填写邀请码，注册
        Sign_url(url=sign_url, headers=headers, sign_text=sign_text)

    # print(invitee_list)
    # a_list = []
    # for i in range(len(invitee_list)):
    #     a_list.append(str(invitee_list[i]))
    # print(a_list)













'''

# # 发送验证码
# sms_body = {"data": {"phone": invitee, "code_type": "SMS_LOGIN"}}
# requests.packages.urllib3.disable_warnings()  # 屏蔽https警告
# response = requests.post(url=sms_url, json=sms_body, headers=headers, verify=False)
# # print(response.status_code)
# # print(response.json()['msg'])
# code = response.json()['data']['code']  # 获取 code
# biz = response.json()['data']['biz']    # 获取biz


# sign   md5加密
md5_text = 'APP_LOGIN' + invitee
m.update(b'%s' % md5_text.encode())
first_md5 = m.hexdigest()
m1.update(b'%s' % first_md5.encode())
last_md5 = m1.hexdigest()


# 验证码登录
login_body = {"data": {"phone": invitee, "code": code, "biz": biz, "sign": last_md5}}
requests.packages.urllib3.disable_warnings()  # 屏蔽https警告
response1 = requests.post(url=login_url, json=login_body, headers=headers, verify=False)
print(response1.status_code)
print(response.json()['msg'])

# print(sign_text)
# sign_body = {"data": {"phone": invitee, "code": globals()['code'], "biz": globals()['biz'], "sign": sign_text, "invite": inviter}}
# requests.packages.urllib3.disable_warnings()
# response2 = requests.post(url=sign_url, json=sign_body, headers=headers, verify=False)
# # print(response2.status_code)
# if 'SUCCESS' in response2.json()['msg']:
#     print('%s 账号创建成功' % invitee)
# else:
#     print('%s 账号的错误细信息： ' % invitee + response2.text)

    # Sign_url(url=sign_url, headers=headers, sign_text=sign_text)

'''
