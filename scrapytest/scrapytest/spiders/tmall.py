# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import Rule


class TmallSpider(scrapy.Spider):
    name = 'tmall'
    allowed_domains = ['detail.tmall.com']
    start_urls = ['https://list.tmall.com/search_product.htm?q=%C1%AC%D2%C2%C8%B9&type=p&style=&redirect=notRedirect&cat=all']
    rules = (
        Rule(SgmlLinkExtractor(allow=(r'https://detail.tmall.com/item.htm?',))),
    )


    def parse(self, response):
        current_url = response.url
        body = response.body
        unicode_body = response.body_as_unicode()  # 返回的html unicode编码
        print current_url

