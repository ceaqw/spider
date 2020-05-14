# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PartjobItem(scrapy.Item):
    name = scrapy.Field()
    job_time = scrapy.Field()
    job_type = scrapy.Field()
    salary = scrapy.Field()
    pay_method = scrapy.Field()
    address = scrapy.Field()
    num = scrapy.Field()
    job_detail = scrapy.Field()
    salary_detail = scrapy.Field()
    job_time_detail = scrapy.Field()
    address_detail = scrapy.Field()
