# -*- coding: utf-8 -*-
import scrapy
import re

from .. import items

PAGE = 1

class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_domain = "https://www.qiushibaike.com"

    def parse(self, response):
        global PAGE
        print("---------->第%d页" % PAGE)
        PAGE += 1
        content_list = response.xpath("//div[contains(@class, 'old-style-col1')]//div")

        for content in content_list:
            author = "".join(content.xpath(".//h2//text()").getall()).strip()
            contents = content.xpath(".//div[@class='content']/span//text()").getall()
            contents = "".join(contents).strip()
            if contents != "":
                yield items.QsbkGetItem(author=author, content=contents)
                # print(contents)

        next_url = response.xpath("//span[@class='next']/../@href").get()

        if next_url:
            yield scrapy.Request(
                url=self.base_domain + next_url,
                callback=self.parse
            )
        else:
            return
