# -*- coding:utf-8 -*-
# @Time     :2019/4/23 18:05
# @Author   :LW
# @File     :1tu.py

import requests
import os
from bs4 import BeautifulSoup
import re, time


def get_page_num(url, headers):
    # 进入首页，获取总共多少页
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    channel = soup.find('a', attrs={'class': 'last'})
    last_num = channel.get_text()
    return last_num, response


def get_html(response):
    html_all = re.findall('<a href="(.*?)"', response.text, re.S)
    new_html = []
    for key in html_all:
        new_key = re.findall('(.*?).html', key, re.S)
        if len(new_key) > 0:
            new_html.append(new_key[0])
    return new_html


def connect_html(url, headers):
    response = requests.get(url, headers=headers)
    img_url = re.findall('<a href="(.*?).webp"', response.text, re.S)
    print(1)

    print(img_url)
    if img_url is None:
        return None
    else:
        for i in range(len(img_url)):
            if 'http://1tu.life/wp-content/uploads/' in img_url[i]:
                img_url1 = img_url[i]
                print(img_url1)
                return img_url1


def save_img(url, headers, img_url):
    img_title = img_url[35:]
    img_path = os.getcwd() + '\\' + img_title
    if not os.path.exists(img_path):
        with open(img_path, 'wb') as f:
            f.write(requests.get(url=url + ".webp", headers=headers).content)
            print('{}----------图片创建成功'.format(img_title))
    else:
        print('{}----------图片创建失败，已存在'.format(img_title))


if __name__ == '__main__':
    url = 'http://1tu.life'
    url_num = 'http://1tu.life/page/'

    cookie = 'splash_i=false; Hm_lvt_b5d455f591a92c984d0dc1b5133dbe30=1554901261,1555079784,1555251828; UM_distinctid=16a3af1994931-0a5979e681e7dd-36664c08-1fa400-16a3af1994b1c1; CNZZDATA1272353405=733715410-1555763110-%7C1556013198'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'

    headers = {
        'Cookie': cookie,
        'User-Agent': user_agent
    }
    page_num = get_page_num(url=url, headers=headers)[0]
    print("本次查询一共有{}页数据".format(page_num))
    print("请输入你想要结束的页码")
    print("输入完成后，请按回车键")
    num = input("请输入结束页码: ")
    print('-----')

    if int(num) >= 1:
        if int(num) == 1:
            html = get_html(response=get_page_num(url=url, headers=headers)[1])
            for i in range(len(html)):
                print(html[i])
                img_url = connect_html(url=html[i] + '.html', headers=headers)
                print(img_url)
                # time.sleep(1)
                if img_url is not None:
                    save_img(url=img_url, headers=headers, img_url=img_url)
        if int(num) > 1:
            pass
    else:
        print("页码输入错误，不执行本程序！")
