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
        uibox_list = response.xpath("//div[@class='uibox']")[1:]
        for uibox in uibox_list:
            print("进度--------->%d//%d" % (uibox_list.index(uibox)+1, len(uibox_list)))
            part_name = uibox.xpath("./div/a/text()").extract_first()
            # print(part_name)
            urls = uibox.xpath(".//li//img/@src").getall()
            urls = [urllib.parse.urljoin(self.start_urls[0], image_url) for image_url in urls]
            # print(urls)
            item = BmwPicItem(part_name=part_name, urls=urls)
            yield item
