# -*- coding:gbk -*-
# @Time     :2019/5/2 21:51    
# @Author   :LW                 
# @File     :1.py
import requests
import datetime
import json
'''
url = 'https://cdn.zyw605.org/guochan/20180624/uijRiaP6/index.m3u8'
# url = 'https://cdn.zyw605.org/guochan/20180624/uijRiaP6/1000kb/hls/index.m3u8'

response = requests.get(url)
print(response.content)

# with open('1.m3u8', 'wb')as f:
#     f.write(response.content)
#     f.close()

# 读取m3u8实际地址
with open('1.m3u8', 'r')as f_read:
    read_f = f_read.readlines()
    for read in read_f:
        if 'm3u8' in read:
            print(read)
            read_new = read
    f_read.close()


url_new = f'https://cdn.zyw605.org/guochan/20180624/uijRiaP6/{read_new}'

response_new = requests.get(url_new)
print(type(response_new.content))
with open('2.m3u8', 'wb')as f:
    f.write(response_new.content)
    f.close()
# json_load = json.loads(response_new.content)
# print(json_load)

with open('2.m3u8', 'r')as f_read:
    read_f = f_read.readlines()
    # for read in read_f:
        # if 'ts' in read:
            # print(read)
            # read_new = read
    f_read.close()
'''
