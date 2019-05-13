# coding:utf-8

from appium import webdriver
import os
import time

device = '127.0.0.1:62001'  # 设备号
pack = 'cn.iiibest.app'  # app的package名称
activity = 'com.ibuyproject.MainActivity'  # app的主activity

# PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

desired_caps = {}
desired_caps['device'] = 'android'
desired_caps['platformName'] = 'Android'
# desired_caps['browserName'] = ''
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = device
desired_caps['appPackage'] = pack
desired_caps['appActivity'] = activity
# 这时候就在手机/模拟器上打开了该app
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(2)
# a = driver.find_element_by_android_uiautomator(uia_string=)
# print(a)
# 点击使用密码登录
loc_text = 'new UiSelector().text(" 使用密码登录 ")'
driver.find_element_by_android_uiautomator(loc_text).click()

time.sleep(2)

# phonenumber_text = 'new UiSelector().text("请输入手机号")'
# passnumber_text = 'new UiSelector().text("")'
# driver.find_element_by_android_uiautomator(phonenumber_text).send_keys('13511111111')


mimas = driver.find_elements_by_class_name('android.widget.EditText')
# for i in len(mimas):
#     print(mimas[i])
print(mimas)
mimas[1].send_keys('123456')

time.sleep(2)

driver.quit()

# [<appium.webdriver.webelement.WebElement (session="0ce06597-46cf-4410-98f0-3d0a8324682a", element="2")>, <appium.webdriver.webelement.WebElement (session="0ce06597-46cf-4410-98f0-3d0a8324682a", element="3")>]
