# -*- coding:utf-8 -*-          
# @Time     :2019/5/14 11:35    
# @Author   :LW                 
# @File     :yunji.py         


import requests
import pprint
# get方法

url = 'https://ys.yunjiglobal.com/yunjiysapp/app/categoryguide/getListItemByCategoryId?'

page = 0    # 页码
categoryid = 0

dt = {
    'ticket': 'ticket|consumer_ticket_100039513_28c02665df70d0f3cd1cfb3d386b3709',
    'pageSize': '10',
    'categoryLevelId3': categoryid,     # 分类id，变量
    'strVersion': '0',
    'appCont': '2',
    'pageIndex': page,      # 页码，变量
    'orderType': ''
}

headers = {
    'Cookie': 'ticket|consumer_ticket_100039513_28c02665df70d0f3cd1cfb3d386b3709',
    'User-Agent': 'appVersion:3.68.0427;mcc_mnc:460_02'
}

response = requests.get(
    url,
    headers=headers,
    params=dt
)
