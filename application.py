#!/usr/bin/python env
# coding: utf-8

from selenium.webdriver.common.keys import Keys

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.mogujie.com")

print driver
assert u"蘑菇街-我的买手街" in driver.title
elem = driver.find_element_by_name("q")
print elem

elem.clear()
elem.send_keys(u"连衣裙")

elem.send_keys(Keys.RETURN)

driver.close()






