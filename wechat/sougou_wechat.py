# -*- coding:utf-8 -*-          
# @Time     :2019/5/18 15:34    
# @Author   :LW                 
# @File     :sougou_wechat.py         

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait as wait
import datetime


def open_chrome():
    """打开浏览器并登录"""
    # 打开浏览器
    driver = webdriver.Chrome()
    return driver


def login(driver):
    url = 'https://weixin.sogou.com/'
    driver.get(url)
    time.sleep(3)
    driver.maximize_window()  # 最大化窗口
    driver.find_element_by_id('loginBtn').click()  # 点击登录按钮
    now = datetime.datetime.now().replace(microsecond=0)
    print(f'{now} --- 正在登录')
    time.sleep(3)
    wait(driver, 60).until_not(lambda x: x.find_element_by_class_name('qrcode lightBorder'))
    now1 = datetime.datetime.now().replace(microsecond=0)
    print(f'{now1} --- 登录成功~')
    time.sleep(3)


def search_wx(driver, key):
    driver.find_element_by_id('query').clear()
    driver.find_element_by_id('query').send_keys(key)
    time.sleep(2)
    driver.find_element_by_class_name('swz2').click()   # 点击 搜公众号
    time.sleep(3)
    nei(driver, key)


def nei(driver, key):
    messages = driver.find_element_by_class_name('news-list2').find_elements_by_tag_name('li')
    names = driver.find_elements_by_class_name('tit')
    # print(len(names))
    weixinhao = driver.find_elements_by_class_name('info')
    # yuefawen = driver.find_elements_by_class_name('line-s')
    # print(lists)
    for line in range(len(messages)):
        wx_name = names[line].find_element_by_tag_name('a').text
        wxh = weixinhao[line].find_element_by_tag_name('label').text
        # yfw = yuefawen[line].text
        message = messages[line].find_elements_by_tag_name('dl')
        if len(message) < 2:
            rz = ' '
        else:
            for messag in range(len(message)):

                if messag == 1:
                    mess = message[messag].text
                    if mess.startswith('微信认证'):
                        rz = mess.split('\n')[-1]
                    else:
                        rz = ' '

        write(wx_name, wxh, rz, key)


def next_page(driver, key):
    n = 1
    while n == 1:
        # time.sleep(5)
        # driver.find_element_by_id('sogou_next').click()
        # time.sleep(5)
        # nei(driver, key)
        try:
            driver.find_element_by_id('sogou_next')
            n = 1
            print('还有下一页~~~~')
            time.sleep(5)

            driver.find_element_by_id('sogou_next').click()
            time.sleep(5)
            nei(driver, key)

        except:
            n = 0
            print('没有下一页了')
            print('')


def reset(driver, key):
    driver.find_element_by_id('query').clear()
    driver.find_element_by_id('query').send_keys(key)
    time.sleep(2)
    driver.find_element_by_class_name('swz2').click()  # 点击 搜公众号
    time.sleep(3)
    nei(driver, key)




def Quit(driver):
    driver.quit()


def find_element_exit(driver, id):
    s = driver.find_elements_by_id(id)
    if len(s) == 0:
        return False        # 不存在元素
    elif len(s) == 1:       # 存在元素
        return True
    else:
        print('找到 %s 个元素：%s' % (len(s), id))


def wechat(key):
    driver = open_chrome()
    login(driver)   # 登录微信
    search_wx(driver, key[0])   # 根据关键字开始搜索
    next_page(driver, key[0])
    for n in range(1, len(key)):
        reset(driver, key[n])
        next_page(driver, key[n])
    Quit(driver)


def write(wx_name, wxh, rz, key):
    with open(f'{key}.txt', 'a+', encoding='utf-8') as f:
        f.write(f'{wx_name}，{wxh}，{rz}\n')
        f.close()


if __name__ == '__main__':
    key = ['情感']
    # for n in range(len(key)):
    wechat(key)
