# -*- coding:utf-8 -*-          
# @Time     :2019/4/25 23:52    
# @Author   :LW                 
# @File     :111.py         

import requests
import json
import time

url = 'https://prodapi.51bushou.com/api/mall/productMallList'

headers = {
    'clientInfo': 'iPhone X',
    'User-Agent':'globalscanner',
    'Cookie':'_ggj_token_=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ7XCJhY2NvdW50SWRcIjoxMzA0NjExMDAyLFwiYXR0cmlidXRlc1wiOntcImxvZ2luU3RhdHVzXCI6XCIxXCJ9LFwiZW5jcnlwdEFpZFwiOlwiMEdTU0xzRlc3VFlZbVlaMnJsaFpLdz09XCIsXCJpc0FwcFwiOnRydWUsXCJvc1wiOjEsXCJ2ZXJzaW9uXCI6XCI0LjNcIn0iLCJleHAiOjE1ODg4ODIwODZ9.3gfjg2qizj9RfvkXWLXzNUg3JqWMCo0BYU98wjEAGvg; _ggj_aid_=1304611002',
    'sn':'1-1669442792-1557473382-ef5d021d237448ee8afbdd4082bd680c',
    'channelId':'0',
    'accountId':'1304611002',
    'versionName':'4.30',
    # latitude	30.278128
    # Content-Length	58
    'deviceId':	'A25566BC-460D-41EA-AD08-BDB2976EFE2C',
    # platform	2
    # Connection	keep-alive
    # eid	1
    # longitude	120.007156
    # buildCode	201905012200
    'sessionId':'a79c28ff1e264a44b5fcd5f92659a6db',
    # network	wifi
    # Accept-Language	zh-Hans-CN;q=1
    'osName':'iOS 12.1.4',
    # Accept	*/*
    'Content-Type':	'application/x-www-form-urlencoded',
    # Accept-Encoding	br, gzip, deflate
    'requestId':'3b708d5d19c39abf69b75455ff04e817'
    # gtp	1.5e35.0.0.1557477581638
}
# num = 0
dic = []

for num in range(1, 21):
    d = {
        'id': 94,
        'page': num,
        'pageCount': 100,
        'sequence': 1,
        'sequenceType': 2,
        'type': 7

    }

    response = requests.post(url, headers=headers, data=d, verify=False).json()
    # print(response)
    # print(type(response))
    # response = json.load(response)
    dict_response = response['data']['productMallList']
    json_response = json.dumps(dict_response, ensure_ascii=False)
    # print(json_response)
    with open('C:\\Users\please call me\PycharmProjects\抓取\\a.json', 'a+', encoding='utf-8') as f:
        f.write(json_response)

    # dic.append(dict_response)
    time.sleep(2)
    f.close()


