# -*- coding:utf-8 -*-          
# @Time     :2019/4/25 23:52    
# @Author   :LW                 
# @File     :111.py         

import requests
import json
import time

url = 'https://prodapi.51bushou.com/api/shop/search'

headers = {
    # 'Host': 'prodapi.51bushou.com',
    'clientInfo': 'iPhone X',
    'User-Agent': 'globalscanner',
    'Cookie': '_ggj_token_=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ7XCJhY2NvdW50SWRcIjoxMzA0NjExMDAyLFwiYXR0cmlidXRlc1wiOntcImxvZ2luU3RhdHVzXCI6XCIxXCJ9LFwiZW5jcnlwdEFpZFwiOlwiMEdTU0xzRlc3VFlZbVlaMnJsaFpLdz09XCIsXCJpc0FwcFwiOnRydWUsXCJvc1wiOjEsXCJ2ZXJzaW9uXCI6XCI0LjNcIn0iLCJleHAiOjE1ODg4ODIwODZ9.3gfjg2qizj9RfvkXWLXzNUg3JqWMCo0BYU98wjEAGvg; _ggj_aid_=1304611002',
    'sn': '1-1669442792-1557745513-d258fb8ef59721908fd9e85a5f9471cb',
    'channelId': '0',
    'accountId': '1304611002',
    'versionName': '4.30',
    'latitude': '30.278147',
    # 'Content-Length': '58',
    'deviceId': 'A25566BC-460D-41EA-AD08-BDB2976EFE2C',
    'platform': '2',
    # 'Connection': 'keep-alive',
    'eid': '0',
    'longitude': '120.007152',
    'buildCode': '201905012200',
    'sessionId': 'c297ac6367f047cfa3537afc751583a1',
    # 'network': 'wifi',
    # 'Accept-Language': 'zh-Hans-CN;q=1',
    'osName': 'iOS 12.1.4',
    # 'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Accept-Encoding': 'br, gzip, deflate',
    'requestId': '3d3fcdb6325c2efc5dd23c177ad693e6',
    # 'gtp': '1.9310.0.0.1557745610871'
}
# num = 0
dic = []

# for num in range(1, 10):
shopid = ['3737']
for shop in shopid:
    while 1:
        d = {
            'activityId': '0',
            'index': '1',
            'pageSize': '20',
            'shopId': shop,
            'sortType': 'DESC'
        }

        response = requests.post(url, headers=headers, data=d, verify=False).json()

        # print(response)
        # print(type(response))
        # response = json.load(response)
        dict_response = response['data']['viewList']
        total = response['data']['total']
        yu = total % 20
        print(yu)
        zs = total // 20
        print(zs)
        json_response = json.dumps(dict_response, ensure_ascii=False)
        # print(json_response)
        with open('C:\\Users\please call me\PycharmProjects\ibuy_test\抓取\\a.json', 'w+', encoding='utf-8') as f:
            f.truncate()    # 清空文本
            f.write(json_response)
            f.close()

        # dic.append(dict_response)
        time.sleep(2)
        if yu != 0:
            for i in range(2, zs+2):
                d = {
                    'activityId': '0',
                    'index': f'{i}',
                    'pageSize': '20',
                    'shopId': shop,
                    'sortType': 'DESC'
                }
                # requests.packages.urllib3.disable_warnings()
                response = requests.post(url, headers=headers, data=d, verify=False).json()
                dict_response = response['data']['viewList']
                total = response['data']['total']
                json_response = json.dumps(dict_response, ensure_ascii=False)
                with open('C:\\Users\please call me\PycharmProjects\ibuy_test\抓取\\a.json', 'a+', encoding='utf-8') as f:
                    f.write(json_response)
                    f.close()
                time.sleep(2)
        elif yu == 0:
            for i in range(2, zs + 1):
                d = {
                    'activityId': '0',
                    'index': f'{i}',
                    'pageSize': '20',
                    'shopId': shop,
                    'sortType': 'DESC'
                }
                response = requests.post(url, headers=headers, data=d, verify=False).json()
                dict_response = response['data']['viewList']
                total = response['data']['total']
                json_response = json.dumps(dict_response, ensure_ascii=False)
                with open('C:\\Users\please call me\PycharmProjects\ibuy_test\抓取\\a.json', 'a+', encoding='utf-8') as f:
                    f.write(json_response)
                    f.close()

                time.sleep(2)
        # f.close()

        break



