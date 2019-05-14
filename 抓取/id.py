# -*- coding:utf-8 -*-          
# @Time     :2019/5/14 17:27    
# @Author   :LW                 
# @File     :id.py         
import json
import requests
# 运动户外 37  充值出行 35  图书 38  宠物生活 40

url = 'https://ys.yunjiglobal.com/yunjiysapp/app/categoryguide/queryCategoryData.json?'

headers = {
        'Cookie': 'ticket|consumer_ticket_100039513_28c02665df70d0f3cd1cfb3d386b3709',
        'User-Agent': 'appVersion:3.68.0427;mcc_mnc:460_02'
    }

d = {
    'categoryId': '40',
    'channel': '1'
}

response = requests.get(
    url,
    headers=headers,
    params=d,
    verify=False
).json()
# print(response)
names = []
a = []

lists = response['data']['guideListVOList']
# print(lists)
for i in range(len(lists)):
    name = lists[i]['guideListName']
    da = lists[i]['guideDataVOS']
    for n in range(len(da)):
        guideName = da[n]['guideName']
        names.append(name + '-' + guideName)
        # print(guideName)
        content = da[n]['content'].split(',')[-1]
        a.append(content)
        # print(content)
    # print(da)
    # print(name)

print(names)
print(a)