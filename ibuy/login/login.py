# -*- coding:utf-8 -*-          
# @Time     :2019/5/6 16:10    
# @Author   :LW                 
# @File     :login.py         


from start_appium import start
import time
# driver =
def login_pwd(driver=start.Start_appium()):
    driver.wait_activity('com.ibuyproject.MainActivity', 10)
    time.sleep(10)   # 休眠3s，等待app启动
    loc_text = 'new UiSelector().text(" 使用密码登录 ")'
    driver.find_element_by_android_uiautomator(loc_text).click()
    time.sleep(3)
    loc_text = 'new UiSelector().text("请输入手机号")'
    driver.find_element_by_android_uiautomator(loc_text).send_keys('15211111011')
    time.sleep(2)
    loc_text1 = 'new UiSelector().className("android.widget.EditText")'
    driver.find_elements_by_android_uiautomator(loc_text1)[1].send_keys('123456')
    time.sleep(2)
    loc_text2 = 'new UiSelector().className("android.widget.TextView")'
    driver.find_elements_by_android_uiautomator(loc_text2)[3].click()
    time.sleep(3)
