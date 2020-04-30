# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import WxappspiderItem

NUM = 1

class WxappSpider(CrawlSpider):
    name = 'wxapp'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'.+article-.+\.html'), callback='parse_detail', follow=True)
    )

    def parse_detail(self, response):
        """
        详情页面数据处理
        :param response:
        :return: item
        """
        global NUM

        title = response.xpath("//h1[@class='ph']/text()").get()
        author = response.xpath("//p[@class='authors']/a/text()").get()
        pub_time = response.xpath("//span[@class='time']/text()").get()
        content = response.xpath("//div[@class='blockquote']//text()").get()

        print("第%d个--------->" % NUM, title)
        NUM += 1
        item = WxappspiderItem(title=title, author=author, pub_time=pub_time, content=content)

        yield item
