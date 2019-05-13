# -*- coding:utf-8 -*-
# @Time     :2019/4/16 14:53
# @Author   :LW
# @File     :爱买店.py


from appium import webdriver
import time

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
    driver.wait_activity('com.ibuyproject.MainActivity', 10)
    return driver


def Quit(driver):
    driver.quit()


def login_pwd(driver):
    # time.sleep(3)   # 休眠3s，等待app启动
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


def My_sign(driver):
    loc_text = 'new UiSelector().text("我的")'
    driver.find_element_by_android_uiautomator(loc_text).click()
    time.sleep(2)
    loc_text2 = 'new UiSelector().className("android.widget.ImageView")'
    driver.find_elements_by_android_uiautomator(loc_text2)[1].click()
    time.sleep(2)
    loc_text = 'new UiSelector().text("邀好友签到，领更多奖励金")'
    cc = driver.find_element_by_android_uiautomator(loc_text).get_attribute('name')
    if cc == '邀好友签到，领更多奖励金':
        print('已签到')
    else:
        loc_text = 'new UiSelector().text("去签到")'
        driver.find_element_by_android_uiautomator(loc_text).click()
        time.sleep(2)
        driver.tap((40, 80), 100)
        print('签到成功')


if __name__ == '__main__':
    # 获取driver
    driver = Start_appium()
    # 登录
    login_pwd(driver=driver)
    # 进入我的-签到
    My_sign(driver=driver)
    # 退出
    Quit(driver=driver)


# loc_text = 'new UiSelector().text("会员中心")'
# driver.find_element_by_android_uiautomator(loc_text).click()
# loc_text = 'new UiSelector().className("android.widget.TextView")'
# czz = driver.find_elements_by_android_uiautomator(loc_text)[4].get_attribute("name")
# # print(czz)
# loc_text = 'new UiSelector().className("android.widget.ImageView")'
# driver.find_elements_by_android_uiautomator(loc_text)[1].click()
# time.sleep(2)
# loc_text = 'new UiSelector().text("去签到")'
# driver.find_element_by_android_uiautomator(loc_text).click()

# time.sleep(2)
# loc_text = 'new UiSelector().text("立即签到")'
# driver.find_element_by_android_uiautomator(loc_text).click()
# time.sleep(2)
# driver.tap((40, 80), 100)   # 实在是获取不到元素，只能靠点击关闭按钮坐标了
# time.sleep(2)

# loc_text = 'new UiSelector().text("邀好友签到，领更多奖励金")'
# print(assert driver.find_element_by_android_uiautomator(loc_text))
# assert driver.find_element_by_android_uiautomator(loc_text).text
