# -*- coding:utf-8 -*-          
# @Time     :2019/5/6 16:07    
# @Author   :LW                 
# @File     :start.py         


from appium import webdriver


def Start_appium():
    device = '127.0.0.1:62001'  # 设备号
    pack = 'cn.iiibest.app'  # app的package名称
    activity = 'com.ibuyproject.MainActivity'  # app的主activity
    desired_caps = {}
    desired_caps['device'] = 'android'
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.1'
    desired_caps['deviceName'] = device
    desired_caps['appPackage'] = pack
    desired_caps['appActivity'] = activity
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # time.sleep(8)
    return driver