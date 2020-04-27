# -*- coding: utf-8 -*-
# describe: 抓取对应url连接下面的图片并保存

import urllib.parse
import scrapy
from bmw_pic.items import BmwPicItem


class BmwSpider(scrapy.Spider):
    name = 'bmw'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    def parse(self, response):
        """
        解析函数
        :param response:
        :return:
        """
        uibox_list = response.xpath("//div[@class='uibox']")[1:]
        for uibox in uibox_list:
            print("进度--------->%d//%d" % (uibox_list.index(uibox)+1, len(uibox_list)))
            part_name = uibox.xpath("./div/a/text()").extract_first()
            # print(part_name)
            urls = uibox.xpath(".//li//img/@src").getall()
            urls = [urllib.parse.urljoin(self.start_urls[0], image_url) for image_url in urls]
            # print(urls)
            item = BmwPicItem(part_name=part_name, urls=urls)
            if uibox.xpath(".//li[@class='last']"):
                yield scrapy.Request(
                    url=urllib.parse.urljoin(self.start_urls[0], uibox.xpath(".//li[@class='last']/a/@href").get()),
                    callback=self.get_detail
                )
            else:
                yield item

    def get_detail(self, response):
        """
        解析更多图片页面资源
        :param response:
        :return:
        """
        for url_page in response.xpath("//div[@class='page']//a/@href").getall()[3:-1]:
            yield scrapy.Request(
                url=urllib.parse.urljoin(self.start_urls[0], url_page),
                callback=self.page_deal
            )

    def page_deal(self, response):
        """
        详情页处理函数
        :param response:
        :return:
        """
        print("-------->详情页加载")
        part_name = response.xpath("//div[@class='uibox-title']/text()").getall()[-1]
        urls = response.xpath("//div[contains(@class, 'uibox-con')]//li//img/@src").getall()
        print(part_name)
        item = BmwPicItem(part_name=part_name, urls=[urllib.parse.urljoin(self.start_urls[0], url) for url in urls])

        yield item