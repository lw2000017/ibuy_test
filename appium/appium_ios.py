# -*- coding:utf-8 -*-
# @Time     :2019/06/10  15:30
# @Author   :刘向上
# @File     :appium_ios.py
# @Order    :


from appium import webdriver

# 这样可以安装app，但是无法打开app
driver = webdriver.Remote(
    command_executor='http://0.0.0.0:4723/wd/hub',
    desired_capabilities={
        'platformName': 'iOS',
        'platformVersion': '12.2',
        'deviceName': 'iPhone X',
        'udid': 'f9690e5bb0a6ff04b9108119277d9a56c639841f',
        'app': '/Users/pleasecallme/Downloads/ibuy-test.ipa'
})

driver.quit()
