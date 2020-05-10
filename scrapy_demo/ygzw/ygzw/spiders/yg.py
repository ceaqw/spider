# -*- coding: utf-8 -*-
import scrapy
from ..items import YgzwItem
from urllib import parse


class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    def parse(self, response):
        """
        主解析函数
        :param response:
        :return:
        """
        state_li = response.xpath("//ul[@class='title-state-ul']//li")

        for li in state_li:
            number = li.xpath(".//span[1]/text()").get()
            status = li.xpath(".//span[2]/text()").get().strip()
            title = li.xpath(".//span[3]//text()").get()
            response_time = li.xpath(".//span[4]/text()").get().strip()
            up_time = li.xpath(".//span[5]/text()").get()

            item = YgzwItem()
            item["number"] = number
            item["status"] = status
            item["title"] = title
            item["response_time"] = response_time
            item["up_time"] = up_time

            href = li.xpath(".//span[3]//@href").get()
            href = parse.urljoin(self.start_urls[0], href)
            yield scrapy.Request(
                url=href,
                callback=self.parse_detail,
                meta={"item": item}
            )

    def parse_detail(self, response):
        """
        详细页解析
        :param response:
        :return:
        """
        item = response.meta["item"]
        content = "".join(response.xpath("//div[@class='details-box']//text()").getall()).strip()
        item["content"] = content

        yield item



