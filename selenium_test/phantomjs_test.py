#!/usr/bin/env python
# coding: utf-8
from selenium import webdriver
import time


cap = webdriver.DesiredCapabilities.CHROME
cap['phantomjs.page.settings.loadImages'] = True # 设置浏览器不加载图片
cap['phantomjs.page.settings.userAgent '] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36" #设置useragent
cap['phantomjs.page.settings.diskCache'] = True # 设置浏览器开启缓存

driver = webdriver.PhantomJS(desired_capabilities=cap)
driver.get("http://list.mogujie.com/book/clothing/10053206")
time.sleep(3)

js = "window.scrollTo(0, document.body.scrollHeight)"
driver.execute_script(js)
time.sleep(0.1)

print driver.page_source
driver.close()
