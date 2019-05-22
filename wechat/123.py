# -*- coding:utf-8 -*-          
# @Time     :2019/5/18 17:14    
# @Author   :LW                 
# @File     :123.py         

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://weixin.sogou.com/weixin?query=%E6%83%85%E6%84%9F&_sug_type_=&s_from=input&_sug_=n&type=1&page=1&ie=utf8')
time.sleep(3)
n = 1
while n == 1:
    time.sleep(5)
    driver.find_element_by_id('sogou_next').click()
    time.sleep(5)
    try:
        next = driver.find_element_by_id('sogou_next')
        n = 1
    except:
        n = 0



driver.quit()