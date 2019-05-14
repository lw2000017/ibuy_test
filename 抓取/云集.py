# -*- coding:utf-8 -*-          
# @Time     :2019/5/14 11:35    
# @Author   :LW                 
# @File     :云集.py


import requests
import json
import time


def get_totalCount(category, pages, name):
    url = 'https://ys.yunjiglobal.com/yunjiysapp/app/categoryguide/getListItemByCategoryId?'
    dt = {
        'ticket': 'ticket|consumer_ticket_100039513_28c02665df70d0f3cd1cfb3d386b3709',
        'pageSize': '100',
        'categoryLevelId3': str(category),  # 分类id，变量
        'strVersion': '0',
        'appCont': '2',
        'pageIndex': str(pages),  # 页码，变量
        'orderType': ''
    }

    headers = {
        'Cookie': 'ticket|consumer_ticket_100039513_28c02665df70d0f3cd1cfb3d386b3709',
        'User-Agent': 'appVersion:3.68.0427;mcc_mnc:460_02'
    }
    # requests.packages.urllib3.disable_warnings()
    response = requests.get(
        url,
        headers=headers,
        params=dt,
        verify=False
    )
    totalCount = response.json().get('data').get('totalCount')
    response1 = response.json()     # 获取到请求结果
    lists = response1['data']['itemList']
    json_response = json.dumps(lists, ensure_ascii=False)
    # write(text=json_response)
    with open(f'{name}.json', 'a+', encoding='utf-8')as f:
        f.write(json_response)
        f.close()
    time.sleep(2)
    return totalCount


def get(pages, category, name):
    url = 'https://ys.yunjiglobal.com/yunjiysapp/app/categoryguide/getListItemByCategoryId?'
    dt = {
        'ticket': 'ticket|consumer_ticket_100039513_28c02665df70d0f3cd1cfb3d386b3709',
        'pageSize': '100',
        'categoryLevelId3': str(category),  # 分类id，变量
        'strVersion': '0',
        'appCont': '2',
        'pageIndex': str(pages),  # 页码，变量
        'orderType': ''
    }

    headers = {
        'Cookie': 'ticket|consumer_ticket_100039513_28c02665df70d0f3cd1cfb3d386b3709',
        'User-Agent': 'appVersion:3.68.0427;mcc_mnc:460_02'
    }
    # requests.packages.urllib3.disable_warnings()

    response = requests.get(
        url,
        headers=headers,
        params=dt,
        verify=False
    )
    response1 = response.json()     # 获取到请求结果
    lists = response1['data']['itemList']
    json_response = json.dumps(lists, ensure_ascii=False)
    # write(text=json_response)
    with open(f'{name}.json', 'a+', encoding='utf-8')as f:
        f.write(json_response)
        f.close()
    time.sleep(2)




def truncate_json(name):
    with open(f'{name}.json', 'w+', encoding='utf-8') as f:
        f.truncate()    # 清空文本内容，每个分类都需要重新写入
        f.close()


def trans(name):
    with open(f'{name}.json', 'r', encoding='utf-8') as f_read:
        content = f_read.readlines()
        # print(content)
        # print(len(content))

    with open(f'{name}.json', 'w', encoding='utf-8') as f:
        for a in content:
            new_a = a.replace('}][{', '},{')
            f.write(new_a)
        f.close()


if __name__ == '__main__':
    page = 0    # 页码
    # categoryid = [2811]     # 分类id
    categoryid = ['2885', '2883', '2882']

    categoryname = ['宠物生活-猫狗日用', '宠物生活-宠物零食', '宠物生活-宠物主粮']

    # categoryname = ['羊绒衫']
    excel_name = []
    sheet_name = '热卖'
    path = f'{excel_name}.xls'
    for num in range(len(categoryid)):
        truncate_json(name=categoryname[num])     # 清空文本内容
        count = get_totalCount(pages=page, category=categoryid[num], name=categoryname[num])
        print(count)
        yu = count % 100
        zs = count // 100
        if count <= 100:
            pass
        elif yu != 0:
            '''余数不等于0，访问的页面数需要+1'''
            for z in range(1, zs + 1):
                get(pages=z, category=categoryid[num], name=categoryname[num])
        elif yu == 0:
            '''余数等于0，则只需访问页面数字是整数就可以了'''
            for z in range(1, zs):
                get(pages=z, category=categoryid[num], name=categoryname[num])

        trans(name=categoryname[num])     # 更改文件内容
        print(f'{categoryname[num]}  已完成')
        # time.sleep(5)

