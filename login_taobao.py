#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os
from config import user

"""
模拟浏览器行为，登录淘宝
"""


def current_dir():
    return os.getcwd() + "/"

driver = webdriver.Chrome()

driver.get(u"https://login.taobao.com/member/login.jhtml")
driver.find_element_by_class_name("login-switch").click()
elem_name = driver.find_element_by_name("TPL_username")
elem_name.clear()
elem_name.send_keys(user.get("username"))
elem_pass = driver.find_element_by_name("TPL_password")
elem_pass.clear()
elem_pass.send_keys(user.get("password"))
elem_submit = driver.find_element_by_id("J_SubmitStatic")
elem_submit.submit()

# 等待3秒 浏览器加载完毕
# driver.implicitly_wait(3)
time.sleep(2)


# 模拟点击动作行为
li = driver.find_element_by_class_name("J_MtNavSubTrigger")

p = driver.find_element_by_xpath("//*[@id='J_MtMainNav']/li[2]/div/dl[2]/dd/p[2]/a")

# 点击账户设置 - 修改头像昵称
ActionChains(driver).move_to_element(li).perform()
time.sleep(2)
ActionChains(driver).move_to_element(p).click(p).perform()

# driver.implicitly_wait(2)
time.sleep(3)
# 截图保存
driver.save_screenshot(current_dir() + "1.png")
print driver.current_url
print driver.get_cookies()

# 关闭浏览器
#driver.close()






