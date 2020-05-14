# -*- coding: utf-8 -*-
import scrapy

from ..items import PartjobItem
from urllib import parse
from ..settings import CITY_NAME


class PartSpiderSpider(scrapy.Spider):
    name = 'part_spider'
    allowed_domains = ['doumi.com']
    start_urls = ['https://www.doumi.com/bj/'+CITY_NAME+'/']
    domain = "https://www.doumi.com"
    count = 1

    def parse(self, response):
        """
        数据主页面采集
        :param response: 响应数据
        :return:
        """
        job_list = response.xpath("//div[contains(@class, 'jzList-con')]/div")

        for job in job_list:
            print("第%d页,进度-----------> %d/%d" % (self.count, job_list.index(job), len(job_list)))
            name = job.xpath(".//div[@class='jzList-txt-t']//a/text()").get().strip()
            page_href = job.xpath(".//div[@class='jzList-txt-t']//a/@href").get()
            page_href = parse.urljoin(self.start_urls[0], page_href)
            job_time = job.xpath(".//ul[contains(@class, 'jzList-field')]//li[1]/span/text()").get().strip()
            job_type = job.xpath(".//ul[contains(@class, 'jzList-field')]//li[2]/text()").get().strip()
            address = job.xpath(".//ul[contains(@class, 'jzList-field')]//li[3]/text()").get().strip()
            num = job.xpath(".//ul[contains(@class, 'jzList-field')]//li[1]/text()").get().strip()
            salary = job.xpath(".//div[@class='jzList-salary']//span[1]//text()").getall()
            salary = " ".join(salary)
            pay_method = job.xpath(".//div[@class='jzList-salary']//span[2]/text()").get().strip()

            meta = PartjobItem(
                name=name,
                job_time=job_time,
                job_type=job_type,
                salary=salary,
                pay_method=pay_method,
                address=address,
                num=num,
            )

            yield scrapy.Request(
                url=page_href,
                callback=self.page_detail,
                meta={"meta": meta}
            )

        self.count += 1
        if self.count <= 3:
            yield scrapy.Request(
                url=self.start_urls[0] + "o" + str(self.count),
                callback=self.parse
            )

    def page_detail(self, response):
        """
        详情页处理函数
        :param response:
        :return:
        """
        meta = response.meta["meta"]
        job_detail = response.xpath("//p[@data-name='contentBox']//text()").getall()
        job_detail = [i.strip() for i in job_detail]
        job_detail = "<br/>".join(job_detail)
        salary_detail = response.xpath("//div[contains(@class, 'salary-welfare')]//p/text()").getall()
        job_time_detail = response.xpath("//div[@class='jz-d-l-b'][2]//dl[1]//dd//text()").getall()
        job_time_detail += response.xpath("//div[@class='jz-d-l-b'][2]//dl[3]//dd//text()").getall()
        job_time_detail = [i.strip() for i in job_time_detail]
        address_detail = response.xpath("//div[@id='work-addr-fold']//div/text()").getall()
        address_detail = [i.strip() for i in address_detail]
        meta["job_detail"] = job_detail
        meta["salary_detail"] = salary_detail
        meta["job_time_detail"] = job_time_detail
        meta["address_detail"] = address_detail

        yield meta

