# -*- coding:utf-8 -*-          
# @Time     :2019/5/13 15:41    
# @Author   :LW                 
# @File     :1.py         

# query = ('情感', '健身', '茶', '杭州', '小姐', '种草', '美妆', '学姐', '佳人', '美丽', '姨', '打扮', '剁手', '丫头', '美容', '秘密', '洋气', '气质', '魅', '网红', '优雅', '精致', '纹身', 'tattoo', '故事', '连衣裙', '韩版', '美版')


from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('http://data.xiguaji.com/Home#/Search')

time.sleep(10)

driver.refresh()



print(cookie)

driver.quit()