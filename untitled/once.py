# encoding:utf-8
import requests
import xlrd
import hashlib
import pymysql
import time


# 发送验证码
def Sms(http, invitee, headers):
    url = http + '/site/sms'
    body = {
        "data": {
            "phone": '{}'.format(invitee),
            "code_type": "SMS_LOGIN",
        }
    }
    requests.packages.urllib3.disable_warnings()  # 屏蔽https警告
    response = requests.post(url=url, json=body, headers=headers, verify=False)
    code = response.json()['data']['code']
    biz = response.json()['data']['biz']
    return code, biz


# 填写邀请码，注册
def Sign(http, invitee, code, biz, sign, inviter):
    url = http + '/v22/site/sign'
    body = {
        'data': {
            'phone': '{}'.format(invitee),
            'code': code,
            'biz': biz,
            'sign': sign,
            'invite': '{}'.format(inviter)
        }
    }
    requests.packages.urllib3.disable_warnings()
    response = requests.post(url=url, json=body, headers=headers, verify=False)
    return response


# 连接数据库
def Connect_mysql():

    db = pymysql.connect('ibuyibuy.mysql.rds.aliyuncs.com', 'ibuy_test', 'ibuy9735!$)*', 'ibuy_test_v2')
    cursor = db.cursor()
    return db, cursor


# 修改密码
def Change_pwd(db, cursor, invitee):

    sql = "UPDATE amc_user SET `password` = '14e1b600b1fd579f47433b88e8d85291' WHERE phone = '{}'".format(invitee)

    try:
        cursor.execute(sql)
    except Exception as e:
        db.rollback()
        print('{} ---------- 密码修改失败'.format(invitee))
    else:
        db.commit()
        print('{} ---------- 密码修改成功'.format(invitee))


# 修改成长值为990
def Change_grow_990(db, cursor, invitee):

    sql = "UPDATE amc_user_account SET growth_value = 990 WHERE phone = '{}'".format(invitee)

    try:
        cursor.execute(sql)
    except Exception as e:
        db.rollback()
        print('{} ---------- 成长值修改990失败'.format(invitee))
    else:
        db.commit()
        print('{} ---------- 成长值修改990成功'.format(invitee))


# 修改成长值为990
def Change_grow_1990(db, cursor, invitee):

    sql = "UPDATE amc_user_account SET growth_value = 1990 WHERE phone = '{}'".format(invitee)

    try:
        cursor.execute(sql)
    except Exception as e:
        db.rollback()
        print('{} ---------- 成长值修改1990失败'.format(invitee))
    else:
        db.commit()
        print('{} ---------- 成长值修改1990成功'.format(invitee))


# 关闭数据库
def Close_mysql(db, cursor):

    cursor.close()
    db.close()


# 密码登录
def login_pwd(http, headers, invitee, login_text):
    url = http + '/v22/site/login'
    body = {
        'data': {
            'phone': '{}'.format(invitee),
            'password': '123456',
            'sign': '{}'.format(login_text)
        }
    }
    requests.packages.urllib3.disable_warnings()
    response = requests.post(url=url, json=body, headers=headers, verify=False)
    # print(response.text)
    access_token = response.json()['data']['access_token']
    return str(access_token)


# 分享素材圈
def Share_material(headers, http, access_token):
    url = http + '/material/operation'
    url1 = http + '/product/share-product'
    body = {
        "data": {
            "mid": "22",
            "type": 4},
        "access_token": str(access_token)

    }
    body1 = {
        'data': {
            'id': '22',
            'type': 1
        },
        "access_token": str(access_token)
    }
    requests.packages.urllib3.disable_warnings()
    response = requests.post(url=url, json=body, headers=headers, verify=False)
    response1 = requests.post(url=url1, json=body1,headers=headers, verify=False)
    return response, response1


# 分享商品
def Share_goods(headers, http, access_token):
    url = http + '/product/share-product'

    body = {
        "data": {
            "sku": "2019021753539898775",  # 分享固定的商品
            "type": 0
        },
        "access_token": str(access_token)
    }
    requests.packages.urllib3.disable_warnings()  # 屏蔽https警告
    response = requests.post(url, json=body, headers=headers, verify=False)
    return response


# 分享汇总
def Share():

    # 分享素材圈
    materials = Share_material(headers=headers, http=http, access_token=str(access_token))

    if materials[0].status_code != 200 or materials[1].status_code != 200:
        print('{} ---------- 注册失败'.format(invitee))
    elif materials[0].status_code == 200 and materials[1].status_code == 200:
        if 'SUCCESS' in materials[0].json()['msg']:
            if 'SUCCESS' in materials[1].json()['msg']:
                print('{} ---------- 账号分享素材圈----------{}'.format(invitee, materials[1].json()['msg']))
            else:
                print('{} ---------- 账号分享素材圈----------{}'.format(invitee, materials[1].json()['msg']))
        else:
            print('{} ----------账号分享素材圈----------{}'.format(invitee, materials[0].json()['msg']))

    # 分享商品
    goods = Share_goods(headers, http, access_token)

    if goods.status_code != 200:
        print('{} ---------- 账号分享商品----------{}'.format(invitee, goods.json()['msg']))
    else:
        if 'SUCCESS' in sign.json()['msg']:
            print('{} ---------- 账号分享商品----------{}'.format(invitee, goods.json()['msg']))
        else:
            print('{} ---------- 账号分享商品----------{} '.format(invitee, goods.json()['msg']))


def Judge():
    if sign.status_code != 200:
        print('{} ---------- 注册失败'.format(invitee))
    else:
        if 'SUCCESS' in sign.json()['msg']:
            print('{} ---------- 账号创建成功。'.format(invitee) + ' 他的上级是 {}'.format(inviter))
        else:
            print('%s ---------- 账号的错误细信息： ' % invitee + sign.text)


if __name__ == '__main__':
    http = 'https://apptest.ibuycoinhd.com'

    headers = {
        'Content-Type': 'application/json;charset=utf-8'
    }

    data = xlrd.open_workbook('手机号.xlsx')
    table = data.sheet_by_name('Sheet1')
    rows = table.nrows

    mysql = Connect_mysql()
    db = mysql[0]
    cursor = mysql[1]

    for i in range(1, rows):
        invitee = int(table.row_values(i)[0])  # 被邀请人手机号
        inviter = int(table.row_values(i)[1])  # 邀请人手机号

        login_text = 'APP_LOGIN' + '{}'.format(str(invitee))
        # 两次md5加密
        for p in range(2):
            m = hashlib.md5()
            m.update(b'%s' % login_text.encode())
            login_result = m.hexdigest()
            login_text = login_result

        # 请求发送短信验证码接口
        sms = Sms(http=http, invitee=invitee, headers=headers)
        # 获得验证码和biz
        code = sms[0]
        biz = sms[1]

        sign_text = 'APP_SIGN' + '{}{}'.format(str(invitee), str(code))
        # 对sign_text两次md5加密
        for n in range(2):
            m = hashlib.md5()
            m.update(b'%s' % sign_text.encode())
            sign_result = m.hexdigest()
            sign_text = sign_result
        # 填写邀请码，注册
        sign = Sign(http=http, invitee=invitee, code=code, biz=biz, sign=sign_text, inviter=inviter)

        # 判断注册是否成功
        Judge()

        # 修改密码
        # Change_pwd(db=db, cursor=cursor, invitee=invitee)
        '''
        # 修改成长值990
        Change_grow_990(db=db, cursor=cursor, invitee=invitee)

        # 执行的太快反应不过来，这边就等待1s了
        time.sleep(1)

        # 分享前需要登录
        login = login_pwd(http=http, headers=headers, invitee=invitee, login_text=login_text)
        access_token = login

        for k in range(3):
            Share()     # 分享素材圈和商品
        
        # 修改成长值1990
        Change_grow_1990(db, cursor, invitee)

        for k in range(3):
            Share()'''
    # 关闭数据库连接
    Close_mysql(db=db, cursor=cursor)
    print()
    input('输入任意内容退出....\n')