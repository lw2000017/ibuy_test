# -*- coding:utf-8 -*-          
# __Time__     :2019/5/22 10:21    
# __Author__   :LW                         


import requests
import re
import xlrd
import random
import time
import xlwt
from xlutils.copy import copy
import os


data = xlrd.open_workbook('all.xls')
table = data.sheet_by_name('sheet1')
raw = table.nrows


url = 'http://data.xiguaji.com/Search/SearchAct/?'
cookie = 'ASP.NET_SessionId=1xow3w0hrl5sxjhbzelzdmxc; Qs_lvt_194035=1558677520; Hm_lvt_91a409c98f787c8181d5bb8ee9c535ba=1558677520; XIGUADATA=UserId=4bf2ae7cd260e210&checksum=cac4c4e02f3c&XIGUADATALIMITID=0bde6552d1774ddc8f91d87cf9280c0f; compareArray=[]; mediav=%7B%22eid%22%3A%22163230%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22n%3FA%5BrwLL(%25%3A%609yVM!3A%60%22%2C%22ctn%22%3A%22%22%7D; Qs_pv_194035=226083947325002700%2C380646170830002370%2C1338978785018903600; Hm_lpvt_91a409c98f787c8181d5bb8ee9c535ba=1558677533'

headers = {
    'Cookie': cookie,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}
new_work = xlrd.open_workbook('end.xls')
r_sheet = new_work.sheet_by_index(0)   # 取第一个sheet
# rows = r_sheet.nrows
w_xls = copy(new_work)
sheet_write = w_xls.get_sheet(0)


row0 = ['公众号名称', '微信号', '账号主体', '预估活跃粉丝数', '所属行业']

for j in range(len(row0)):
    sheet_write.write(0, j, row0[j])  # 写入第一行，标题



for i in range(1, raw):
    wxm = table.row_values(i)[0]
    wxh = table.row_values(i)[1]
    key = wxh
    d = {
        'type': '1',
        'key': key,
        'miniAppId': '0'
    }
    if i % 5 == 0:
        print('休息一下~')
        time.sleep(random.randint(1, 5) * 60)

        response = requests.get(
            url,
            headers=headers,
            params=d
        ).text
        # print(response)
    else:
        time.sleep(5)
        response = requests.get(
            url,
            headers=headers,
            params=d
        ).text
        # print(response)
    # 搜索结果
    ssjg = re.findall('class="dn-results icon-search-result">.*?<h6>(.*?)</h6>.*?<div class="search-tips">', response, re.S)
    print(ssjg)

    if len(ssjg) != 0:
        '''说明暂无搜索结果'''
        continue
    else:
        # 账号主体
        zhzt = re.findall('class="number-info">.*?<span>(.*?)</span>', response, re.S)[0].split('\r\n')[-1]     # re.S 忽略换行符
        # print(zhzt)
        if zhzt.startswith(' '):
            zhzt = re.findall('class="number-info">.*?<span>(.*?)<a class', response, re.S)[0].split('\r\n')[-1].split('账号主体：')[-1]
            print(zhzt)
        else:
            zhzt = zhzt.split('账号主体：')[-1]
        # 预估粉丝数
        ygfss = re.findall('class="number-describe-index clearfix">.*?<span>(.*?)</span>', response, re.S)
        # 所属行业
        sshy = re.findall('class="number-describe-item".*?<span>所属行业：</span>(.*?)</p>', response, re.S)[0]
        sheet_write.write(i, 0, wxm)
        sheet_write.write(i, 1, wxh)
        sheet_write.write(i, 2, zhzt)
        sheet_write.write(i, 3, ygfss)
        sheet_write.write(i, 4, sshy)
        w_xls.save('end.xls' + '.out' + os.path.splitext('end.xls')[-1])

# workbook.save('end.xls')
