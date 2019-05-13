# coding:utf-8

import requests
import pymysql
import json
'''
# 连接数据库
db = pymysql.connect('ibuyibuy.mysql.rds.aliyuncs.com', 'ibuy_test', 'ibuy9735!$)*', 'ibuy_test_v2')
# 创建一个游标对象
cursor = db.cursor()
# 查询语句
for i in list:
    value = i
    cursor.execute("SELECT * FROM code_limit WHERE phone = '%value' GROUP BY ctime DESC", value)

# 关闭数据库
db.close()

'''
'''
url_sms = "https://apptest.ibuycoinhd.com/site/sms"
headers = {
    'Content-Type': 'application/json;charset=utf-8'
    # 'user-agent': 'iBuyProject/12 CFNetwork/976 Darwin/18.2.0'
}

body = {"data": {"phone": "13700000000", "code_type": "SMS_LOGIN"}}
payload = json.dumps(body)
# 屏蔽警告
requests.packages.urllib3.disable_warnings()
r = requests.post(url=url_sms, json=body, headers=headers, verify=False)
# 获取验证码
code = r.json()['data']['code']
# 获取验证编码
biz = r.json()['data']['biz']
print(code)
print(biz)



url_login = "https://apptest.ibuycoinhd.com/v22/site/login"
body_login = {"data": {"phone": "13700000000", "code": "502324", "biz": "19040116274824460", "sign": "5d72021910674f541db3617e515b80e1"}}
'''


# 邀请人
inviter = '15888888888'

headers = {
    'Content-Type': 'application/json;charset=utf-8'
}

# from requests.packages.urllib3.exceptions import I
# 第一步，先创建一个被邀请人的手机号
for i in range(1, 101):
    # 数字前补齐0
    k = "%03d" % i
    # print(type(k))
    # 被邀请人手机号
    invitee = "13711111" + k

    # 第一个接口，快捷登录，使用验证码登录
    url_sms = ""    # 验证码登录接口
    body = {}   # 传值
    requests.packages.urllib3.disable_warnings()
    response = requests.post(url=url_sms, json=body, headers=headers, verify=False)
    code = response.json()['data']['']
    biz = response.json()['data']['']
