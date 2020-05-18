# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from urllib import request
import os


class TbSpider(CrawlSpider):
    name = 'tb'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%E6%B8%B8%E6%88%8F&ie=utf-8&cid=&tab=corearea&pn=0']

    rules = (
        Rule(LinkExtractor(allow=r'/p/\d+'), callback='parse_item'),
    )

    def parse_item(self, response):
        """
        解析来凝结处理
        :param response:
        :return:
        """
        item = {}
        item["title"] = response.xpath("//h3/@title").get()
        item["username"] = response.xpath("//a[contains(@class, 'p_author_name')]//text()").get()
        item["video_src"] = response.xpath("//div[@class='video_src_wrapper']//@vhsrc").getall()

        if len(item["video_src"]) > 0:
            print(item["video_src"][0])
            print("正在抓取视频：%s" % item["username"])
            request.urlretrieve(item["video_src"][0], os.path.dirname(__file__)+"/video/"+str(item["username"])+".mp4")
