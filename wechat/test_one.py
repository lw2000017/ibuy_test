# -*- coding:utf-8 -*-          
# @Time     :2019/5/13 11:19    
# @Author   :LW                 
# @File     :test_one.py
# @remarks  :接口请求后需要等待一下，不然，太快的操作容易被微信误会

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait as wait
import time
import json
import requests
import re
import random
import datetime

# 账号和密码
account = 'gh_f5dc6f57c595'
password = 'lw200017..++--'


def wechat():
    print('正在启动浏览器~  骚等~')
    # 启动浏览器
    driver = webdriver.Chrome()
    # 打开微信公众号地址
    driver.get('https://mp.weixin.qq.com/')
    # 最大化窗口
    driver.maximize_window()
    # 清空输入框内容并输入用户名
    driver.find_element_by_name('account').clear()
    driver.find_element_by_name('account').send_keys(account)
    # 清空输入框内容并输入密码
    driver.find_element_by_name('password').clear()
    driver.find_element_by_name('password').send_keys(password)
    # 点击 记住我 复选框
    driver.find_element_by_class_name('icon_checkbox').click()
    # 强制休眠5s，以防太快输入被屏蔽
    time.sleep(5)
    # 点击登录按钮
    driver.find_element_by_class_name('btn_login').click()
    # 强制休息5s，用来扫描二维码？
    print('准备拿出手机扫描二维码了吗？')
    # time.sleep()
    # 检查是否登录成功
    wait(driver, 20).until(lambda x: x.find_element_by_class_name('weui-desktop-operation-group_default'))
    print('登录成功了呢~')
    time.sleep(5)
    # 获取登录成功的cookies
    cookies = driver.get_cookies()
    print(cookies)
    post = {}
    # 获取到的cookies是列表形式，将cookies转换成json形式并存入本地文件中
    for cookie in cookies:
        post[cookie['name']] = cookie['value']
    cookie_str = json.dumps(post)
    with open('cookie.txt', 'w+') as f:
        f.write(cookie_str)
    print('cookie信息以保存到本地！')
    return driver


def get_content(query):
    # 公众号主页
    url = 'https://mp.weixin.qq.com'
    # 设置headers
    headers = {
        'Host': 'mp.weixin.qq.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    }
    # 屏蔽https警告
    requests.packages.urllib3.disable_warnings()

    with open('cookie.txt', 'r') as f:
        cookie = f.read()

    # 转换为字典
    cookies = json.loads(cookie)
    # 增加重试链接次数
    session = requests.session()
    session.keep_alive = False
    session.adapters.DEFAULT_RETRIES = 511
    time.sleep(5)
    # 获取token
    response = session.get(url=url, cookies=cookies, verify=False)
    token = re.findall(r'token=(\d+)', str(response.url))[0]
    time.sleep(2)
    """第一次搜索"""
    # 搜索url，输入公众号关键字进行搜索
    search_url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?'
    # 搜索微信公众号接口需要传入的参数，其中有三个变量：微信公众号token，随机数random，搜索的微信公众号名字
    query_id = {
        'action': 'search_biz',
        'token': token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),
        'query': query,
        'begin': '0',   # 变量，非第一页需要发生变化，每页+5
        'count': '5'
    }

    # 打开搜索微信公众号接口，需要传入相关参数信息：cookies，params，headers
    search_response = session.get(
        search_url,
        cookies=cookies,
        headers=headers,
        params=query_id
    )
    lists = search_response.json()
    total = lists['total']
    print(total)
    zs = total // 5
    print(zs)
    list_list = lists['list']
    get_txt(list_list, query)

    if total > 2000:    # 总数大于2000，但是只返回400页，多余的数据暂时就不要了
        for begin in range(1, 400):
            new_query_id = {
                'action': 'search_biz',
                'token': token,
                'lang': 'zh_CN',
                'f': 'json',
                'ajax': '1',
                'random': random.random(),
                'query': query,
                'begin': f'{begin * 5}',  # 变量，非第一页需要发生变化，每页+5  等于0，就是第一页
                'count': '5'
            }
            # print(begin)
            search_response = session.get(
            search_url,
            cookies=cookies,
            headers=headers,
            params=new_query_id
            )
            lists = search_response.json()
            err_msg = lists['base_resp']['err_msg']
            if err_msg == 'ok':
                list_list = lists['list']

                get_txt(list_list, query)
                time.sleep(3)
            elif err_msg == 'freq control':
                print('正在等待70s')
                time.sleep(70)
                search_response = session.get(
                    search_url,
                    cookies=cookies,
                    headers=headers,
                    params=new_query_id
                )
                lists = search_response.json()
                err_msg = lists['base_resp']['err_msg']
                while err_msg == 'freq control':
                    time.sleep()
                list_list = lists['list']

                get_txt(list_list, query)
                time.sleep(5)
            print(begin * 5)

        print('dayu2000')
    elif total <= 2000:
        for begin in range(1, zs+1):
            new_query_id = {
                'action': 'search_biz',
                'token': token,
                'lang': 'zh_CN',
                'f': 'json',
                'ajax': '1',
                'random': random.random(),
                'query': query,
                'begin': f'{begin * 5}',  # 变量，非第一页需要发生变化，每页+5  等于0，就是第一页
                'count': '5'
            }
            # print(begin)
            search_response = session.get(
                search_url,
                cookies=cookies,
                headers=headers,
                params=new_query_id
            )
            lists = search_response.json()
            err_msg = lists['base_resp']['err_msg']
            if err_msg == 'ok':
                list_list = lists['list']

                get_txt(list_list, query)
                time.sleep(3)
            elif err_msg == 'freq control':
                print('正在等待70s')
                time.sleep(70)
                search_response = session.get(
                    search_url,
                    cookies=cookies,
                    headers=headers,
                    params=new_query_id
                )
                lists = search_response.json()
                print(lists)
                list_list = lists['list']

                get_txt(list_list, query)
                time.sleep(5)
            print(begin * 5)
        print('xiaoyu 2000')

    # 操作太频繁，预计需要等待一分钟左右后才可继续访问


    """

    # 微信公众号文章接口地址
    appmsg_url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?'

    query_id_data = {
        'token': token,
        'lang': 'zn_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),
        'action': 'list_ex',
        'begin': '0',   # 不同页，此参数不同
        'count': '5',
        'query': '',
        'fakeid': fakeid,
        'type': '9'
    }

    appmsg_response = session.get(
        appmsg_url,
        cookies=cookies,
        headers=headers,
        params=query_id_data)

    # 获取总文章总数量
    max_num = appmsg_response.json().get('app_msg_cnt')
    # 最后一页
    begin = int(max_num - 5)

    if begin > 0:
        query_id_data = {
            'token': token,
            'lang': 'zn_CN',
            'f': 'json',
            'ajax': '1',
            'random': random.random(),
            'action': 'list_ex',
            'begin': '0',  # 不同页，此参数不同
            'count': '5',
            'query': '',
            'fakeid': fakeid,
            'type': '9'
        }
        print('正在请求最后一页')
        time.sleep(5)

        """


def get_txt(list_list, query):
    for i in range(len(list_list)):
        fakeid = list_list[i]['fakeid']  # fakeid 公众号id
        nickname = list_list[i]['nickname']  # 微信名称
        alias = list_list[i]['alias']  # 微信号
        service_type = list_list[i]['service_type']  # 公众号类型
        print(fakeid)
        write_txt(fakeid, nickname, alias, service_type, query)



def chrome_quit():
    driver = wechat()
    driver.quit()



def write_txt(fakeid, nickname, alias, service_type, query):
    with open('情感1.txt', 'a+', encoding='utf-8') as f:
        f.write(f'{fakeid}，{nickname}，{alias}，{service_type}，{query}\n')
        f.close()


if __name__ == '__main__':
    now = datetime.datetime.now().replace(second=0)
    # 获取到登录cookie
    chrome_quit()
    now_new = datetime.datetime.now().replace(second=0)
    # query 关键字
    # query = ['情感', '健身', '茶', '杭州', '小姐', '种草', '美妆', '学姐', '佳人', '美丽', '姨', '打扮', '剁手', '丫头', '美容', '秘密', '洋气', '气质', '魅', '网红', '优雅', '精致', '纹身', 'tattoo', '故事', '连衣裙', '韩版', '美版']
    query = '情感'
    get_content(query=query)
