#!/usr/bin/env python
# coding: utf-8

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


def next_page(browser):
    browser.find_element_by_partial_link_text(u"下一页").click()


def scroll(browser, height):
    js = "window.scrollTo(0, {0})".format(height)
    browser.execute_script(js)
    time.sleep(0.1)


def get_page_goods_info(browser):
    # 慢慢移动到底部
    height = 100
    size = 0
    good_item_list = browser.find_elements_by_class_name("goods_item")
    for good_item in good_item_list:
        size += 1
        if size % 5 == 0:
            height += 600 * 2
            scroll(browser, height)
        good_info = dict()
        good_info["trade_item_id_str"] = good_item.get_attribute("data-tradeitemid")
        try:
            like_link_elem = good_item.find_element(By.CLASS_NAME, "likeLink")
            good_info["like_link"] = like_link_elem.get_attribute("href")
        except NoSuchElementException:
            pass
        #  详情页链接和图片链接
        try:
            detail = good_item.find_element(By.CLASS_NAME, "J_dynamic_imagebox")
            good_info["detail_page_url"] = detail.get_attribute("href")
            good_info["img_jpg"] = detail.get_attribute("img-src")
            try:
                img_webp = good_item.find_element(By.CLASS_NAME, "J_dynamic_img")
                good_info["img_webp"] = img_webp.get_attribute("src")
            except Exception as ex:
                print ex
        except NoSuchElementException as ee:
            print ee

        # 标题和价格
        try:
            title = good_item.find_element(By.CLASS_NAME, "title")
            good_info["title"] = title.text
            price_info = good_item.find_element(By.CLASS_NAME, "price_info")
            good_info["price_info"] = price_info.text
            good_info["fav_num"] = good_item.find_element(By.CLASS_NAME, "fav_num").text
        except Exception as e:
            print e

        try:
            good_info["org_price"] = good_item.find_element(By.CLASS_NAME, "org_price").find_element(By.TAG_NAME, "span").text
        except Exception as e:
            print e

        format_print(good_info)


def format_print(info):
    print "标题:", info["title"]
    print "详情页链接:", info["detail_page_url"]
    print "相似商品:", info["like_link"] if info.has_key("like_link") else "暂无相似商品"
    print "图片jpg:", info["img_jpg"]
    print "图片webp:", info["img_webp"]
    print "喜欢:", info["fav_num"]
    print "折扣价:", info["price_info"]
    print "原价:", info["org_price"] if info.has_key("org_price") else "无折扣"
    print


driver = webdriver.Chrome()
driver.maximize_window()
driver.get(u"http://www.mogujie.com")

assert u"蘑菇街-我的买手街" in driver.title
elem = driver.find_element_by_name("q")

elem.clear()
elem.send_keys(u"连衣裙")
elem.send_keys(Keys.RETURN)
time.sleep(2)

index = 5
while index > 0:
    try:
        get_page_goods_info(driver)
        next_page(browser=driver)
    except Exception as exception:
        index -= 1
        print exception


# 关闭浏览器
driver.close()












