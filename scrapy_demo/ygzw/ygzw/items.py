# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YgzwItem(scrapy.Item):
    number = scrapy.Field()
    status = scrapy.Field()
    title = scrapy.Field()
    response_time = scrapy.Field()
    up_time = scrapy.Field()
    content = scrapy.Field()
