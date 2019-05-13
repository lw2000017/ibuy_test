# coding:utf-8
import requests
import hashlib
import xlrd


# 登录
def Login_url(url, headers, login_text):
    login_body = {
        "data": {"phone": '{}'.format(invitee),
                 "password": '123456',
                 "sign": '{}'.format(login_text)
                 }
    }
    requests.packages.urllib3.disable_warnings()  # 屏蔽https警告
    response = requests.post(url=url, headers=headers, json=login_body, verify=False)
    globals()['access_token'] = response.json()['data']['access_token']  # 获取token
    # print(globals()['access_token'])


# 分享素材圈
def Operation(headers):

    opera_url = 'https://apptest.ibuycoinhd.com/material/operation'  # 分享url
    opera_url1 = 'https://apptest.ibuycoinhd.com/product/share-product'
    access_token = globals()['access_token']
    opera_body = {
        "data": {
            "mid": "22",
            "type": 4},
        "access_token": str(access_token)

    }
    opera_body1 = {
        'data': {
            'id': '22',
            'type': 1
        },
        "access_token": str(access_token)
    }
    requests.packages.urllib3.disable_warnings()  # 屏蔽https警告
    response = requests.post(url=opera_url, json=opera_body, headers=headers, verify=False)
    response1 = requests.post(url=opera_url1, json=opera_body1, headers=headers, verify=False)
    if 'SUCCESS' in response.json()['msg']:
        if 'SUCCESS' in response1.json()['msg']:
            print('{} 账号分享素材圈---{}'.format(invitee, response.json()['msg']))
    else:
        print('{} 账号分享素材圈---{}'.format(invitee, response.json()['msg']))


# 分享商品
def Share_shop(headers):
    url = 'https://apptest.ibuycoinhd.com/product/share-product'

    access_token = globals()['access_token']

    body = {
        "data": {
            "sku": "2019021753539898775",  # 分享固定的商品
            "type": 0
        },
        "access_token": str(access_token)
    }
    requests.packages.urllib3.disable_warnings()  # 屏蔽https警告
    response = requests.post(url, json=body, headers=headers, verify=False)

    if 'SUCCESS' in response.json()['msg']:
        print('{} 账号分享商品---{}'.format(invitee, response.json()['msg']))
    else:
        print('{} 账号分享商品---{}'.format(invitee, response.json()['msg']))


if __name__ == '__main__':

    login_url = 'https://apptest.ibuycoinhd.com/v22/site/login'  # 手机密码登录

    headers = {
        'Content-Type': 'application/json;charset=utf-8'
    }
    globals()['access_token'] = None

    data = xlrd.open_workbook('手机号.xlsx')  # 打开在该脚本路径下的excel文件，如果需要其他路径，把其他路径复制上即可
    table = data.sheet_by_name('Sheet5')  # 获取某个sheet内容
    rows = table.nrows  # 获取总行数

    for i in range(1, rows):
        invitee = int(table.row_values(i)[0])  # 需要分享的人的手机号
        # inviter = int(table.row_values(i)[1])  # 邀请人手机号

        login_text = 'APP_LOGIN' + '{}'.format(invitee)

        for i in range(2):
            m = hashlib.md5()
            m.update(b'%s' % login_text.encode())
            login_result = m.hexdigest()
            login_text = login_result

        # 登录
        Login_url(url=login_url, headers=headers, login_text=login_text)

        for i in range(3):
            # 分享素材圈
            Operation(headers=headers)
            # 分享商品
            Share_shop(headers=headers)

