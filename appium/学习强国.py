# coding:utf-8

from appium import webdriver
import os
import time


# def Start_appium():
    
device = '127.0.0.1:62001'  # 设备号
pack = 'cn.xuexi.android'     # app的package名称
activity = 'com.alibaba.android.rimet.biz.SplashActivity'   # app的主activity
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
time.sleep(10)
# a = driver.find_element_by_android_uiautomator(uia_string=)
print('输入账号')
driver.find_element_by_id('cn.xuexi.android:id/et_phone_input').send_keys('13837015054')
time.sleep(2)
driver.find_element_by_id('cn.xuexi.android:id/et_pwd_login').send_keys('12345678')

time.sleep(2)
driver.find_element_by_id('cn.xuexi.android:id/btn_next').click()
# print(a)

print(1234)

time.sleep(2)


# 点击同意坐标
driver.find_element_by_xpath('//android.view.View[@content-desc="同意"]').click()


time.sleep(2)
driver.quit()

