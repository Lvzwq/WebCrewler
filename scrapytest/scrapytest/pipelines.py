# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapytestPipeline(object):

    def process_item(self, item, spider):
        print "商品名称", item.get("GOODS_NAME")
        print "商品单价", item.get("GOODS_PRICE")
        print "商品详情页链接", item.get("GOODS_URL")
        print "商品月销量", item.get("MONTHLY_SALES")
        pass
