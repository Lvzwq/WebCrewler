#!/usr/bin/python env
# coding:  utf-8
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

selenium_grid_url = "http://0.0.0.0:4444/wd/hub"

# Create a desired capabilities object as a starting point.
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['platform'] = "MAC"
capabilities['version'] = "59.0.3071.115"

# Instantiate an instance of Remote WebDriver with the desired capabilities.
driver = webdriver.Remote(desired_capabilities=capabilities, command_executor=selenium_grid_url)
