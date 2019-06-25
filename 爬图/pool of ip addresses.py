# -*- coding:utf-8 -*-
# @Time     :2019/06/24  11:13
# @Author   :刘向上
# @File     :pool of ip addresses.py
# @explain  :ip代理池

import requests
import urllib3
import urllib.request
import re
import time
from bs4 import BeautifulSoup


"""
url = 'https://www.xicidaili.com/nn/'
User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/75.0.3770.100 Safari/537.36'
Cookie = '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWUzNmE5ODc0NDFmMTU2ZTQyNzUyZDkwYTJhNTY5M' \
         'GUxBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXdlSmN2b2JBY2ZReW5IQjF3OFFGYkpTOEhPcklwQmNnb1NMbFR6OFpZd2' \
         'M9BjsARg%3D%3D--e1efe0789dbc912d90f3b1efcfa9f437466ec782; Hm_lvt_0cf76c77469e965d2957f0553e6e' \
         'cf59=1561345865; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1561345865'
headers = {
    'User-Agent': User_Agent,
    'Cookie': Cookie
}

urllib3.disable_warnings()
res = requests.get(url=url, headers=headers, verify=False)
# print(res.text)
print(res.status_code)

# ip_address_port_list = re.findall('<img src="//fs.xicidaili.com/images/flag/cn.png" alt="Cn">'
#                                   '/n/t</td>/n/t<td>(.*?)</td>/n/t<td>/d+</td>', res.text, re.S)
# print(ip_address_port_list)


soup = BeautifulSoup(res.text, 'html.parser')
ips = soup.find_all('tr')
ip_list = []

for i in range(1, len(ips)):
    ip_info = ips[i]
    tds = ip_info.find_all('td')
    ip_list.append(tds[1].text + ':' + tds[2].text)

print(ip_list)

with open('ip_pool.txt', 'w') as f:
    for ip in ip_list:
        f.write(ip)
        f.write('\n')

    f.close()

"""

User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/75.0.3770.100 Safari/537.36'
# Cookie = '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWUzNmE5ODc0NDFmMTU2ZTQyNzUyZDkwYTJhNTY5M' \
#          'GUxBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXdlSmN2b2JBY2ZReW5IQjF3OFFGYkpTOEhPcklwQmNnb1NMbFR6OFpZd2' \
#          'M9BjsARg%3D%3D--e1efe0789dbc912d90f3b1efcfa9f437466ec782; Hm_lvt_0cf76c77469e965d2957f0553e6e' \
#          'cf59=1561345865; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1561345865'
headers = {
    'User-Agent': User_Agent
    # 'Cookie': Cookie
}


with open('ip_pool.txt', 'r') as f:
    f_re = f.readlines()
    f.close()

for i in range(len(f_re)):
    ip = f_re[i].split('\n')[0]
    print(ip)
    ip_parms = {"http": 'http://' + ip, "https": 'https://' + ip}
    urllib3.disable_warnings()
    try:
        res = requests.get(url='https://www.baidu.com', proxies=ip_parms, headers=headers, timeout=5, verify=False).status_code
        print(res)
    except:
        print('timeout')




