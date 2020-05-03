# -*- coding: utf-8 -*-
import scrapy
from ..items import SinaSpiderItem

class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        news_li = response.xpath("//div[@data-sudaclick='newsnav']//li")
        for news_page in news_li:
            types = news_page.xpath(".//text()").get()
            news_href = news_page.xpath(".//@href").get()
            print("请求的url-------->", news_href)

            item = SinaSpiderItem(com_types="新闻", types=types)
            yield scrapy.Request(
                url=news_href,
                meta={"item": item},
                callback=self.href_page
            )

    def href_page(self, response):
        """
        详情链接页面处理
        :param response:
        :return:
        """
        meta_item = response.meta.get("item")
        detail_url = response.xpath("//div[@class='right-content']//li")

        for detail in detail_url:
            detail_title = detail.xpath(".//text()").get()
            detail_url = detail.xpath(".//@href").get()
            meta_item["detail_title"] = detail_title
            meta_item["detail_url"] = detail_url

            yield meta_item