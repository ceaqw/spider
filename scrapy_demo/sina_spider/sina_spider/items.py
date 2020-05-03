# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaSpiderItem(scrapy.Item):
    com_types = scrapy.Field()
    types = scrapy.Field()
    detail_title = scrapy.Field()
    detail_url = scrapy.Field()
