# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from ..items import TmallItem


class TmallSpider(scrapy.Spider):
    name = "tmall"
    allowed_domains = ['detail.tmall.com', 'list.tmall.com']
    # start_urls = ['https://list.tmall.com/search_product.htm?q=%C1%AC%D2%C2%C8%B9&type=p&style=&redirect=notRedirect&cat=all']
    start_urls = ["https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.aVNGHZ&cat=53320010&sort=d&style=g&active=1&industryCatId=53320010&theme=663&type=pc"]

    cookie = {
        'cookie2': '1108b449df9d3cbb408d0fc46d853dec',
        't': '87ffe9059838bdb792fcab55783f707e',
        '_tb_token_': 'f164f1be7939'
    }


    def start_requests(self):
        header = {
            # ":authority": "list.tmall.com",
            # ":method": "GET",
            # ":path": "/search_product.htm?spm=a220m.1000858.0.0.aVNGHZ&cat=53320010&sort=d&style=g&active=1&industryCatId=53320010&theme=663&type=pc",
            # ":scheme": "https",
            "Host": "list.tmall.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Cache-Control": "max-age=0",
            "Referer": "https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.aVNGHZ&cat=53320010&sort=d&style=g&active=1&industryCatId=53320010&theme=663&type=pc",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
            "Upgrade-Insecure-Requests": "1",
        }


        print header
        return [scrapy.Request(self.start_urls[0], headers=header, callback=self.parse, cookies=self.cookie)]

    def parse(self, response):
        divs = response.xpath('//div[@id="J_ItemList"]/div')
        print("items len = %d" % len(divs))
        for div in divs:
            item = TmallItem()
            # 价格
            item['GOODS_PRICE'] = div.xpath('div/p[1]/em/text()').extract_first()
            # 月销量
            item['MONTHLY_SALES'] = div.xpath('div/p[2]/span[1]/em/text()').extract_first()
            # url
            good_url = div.xpath('div/div[2]/a[1]/@href').extract_first()
            if not 'http' in good_url:
                good_url = response.urljoin(good_url)
            item['GOODS_URL'] = good_url

            # 进入店里面
            yield scrapy.Request(url=good_url, meta={'item': item}, callback=self.detail_parse)
        next_page = response.urljoin(response.xpath('//a[@class="ui-page-next"]/@href').extract_first())
        yield scrapy.Request(url=next_page, callback=self.parse, cookies=self.cookie)

    def detail_parse(self, response):
        # 获取item
        item = response.meta['item']
        # 商品名称
        item['GOODS_NAME'] = response.xpath(
            '//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[1]/h1/a/text()').extract_first()
        yield item
