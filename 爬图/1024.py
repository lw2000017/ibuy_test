# -*- coding:utf-8 -*-          
# __Time__     :2019/6/2 21:16    
# __Author__   :LW                         

import requests
import re


url = 'http://c1.h9e4924effb.xyz/pw/thread.php'
index_url = 'http://c1.h9e4924effb.xyz/pw/html_data/'
userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.204 Safari/537.36'
cookie = '__cfduid=d01b412360d18341906dde5c51e54787e1559475621; ' \
         'UM_distinctid=16b18040d29d54-0e790f1512fedd-9353769-1fa400-16b18040d2a9ba; ' \
         'aafaf_lastpos=F111; aafaf_threadlog=%2C111%2C; aafaf_ol_offset=417488; ' \
         'CNZZDATA1261158850=285419257-1559470846-null%7C1559476246; ' \
         'aafaf_lastvisit=136%091559481253%09%2Fpw%2Fthread.php%3Ffid%3D111%26page%3D1'
headers = {
    'Cookie': cookie,
    'User-Agent': userAgent,
    'Accept-Language': 'zh-CN,zh;q=0.9'
}
page = 1
d = {
    'fid': 111,
    'page': page
}


# response = requests.get(
#     url,
#     headers=headers,
#     params=d
# ).content.decode('utf-8')

# print(response)

# href_and_title = re.findall('<a href="html_data/(.*?)" id="a_ajax_.*?">(.*?)</a>', response, re.S)

# print(href_and_title[1][0])

uu = 'http://c1.h9e4924effb.xyz/pw/html_data/111/1906/4143978.html'

response1 = requests.get(
    uu,
    headers=headers
    # params=d
).content.decode('utf-8')

# print(response1)

from selenium import webdriver

driver = webdriver.PhantomJS()

driver.get(uu)

print(driver.page_source)

# a = driver.get_screenshot_as_file('1.jpg')

driver.quit()
