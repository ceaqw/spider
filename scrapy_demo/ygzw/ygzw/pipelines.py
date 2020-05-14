# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
# from .settings import MONGO_HOST


class YgzwPipeline(object):
    def __init__(self):
        super(YgzwPipeline, self).__init__()

        self.collection = MongoClient()["test"]["test"]

    def process_item(self, item, spider):

        self.collection.insert(dict(item))
        return item