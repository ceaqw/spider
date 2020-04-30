# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv


class QsbkGetPipeline(object):
    def __init__(self):
        self.fp = open("qsbk.csv", "w", encoding="utf8")
        self.csv_write = csv.DictWriter(self.fp, ["author", "content"])
        self.csv_write.writeheader()

    def open_spider(self, spider):
        """
        爬中开始自动调用
        :param spider:
        :return:
        """
        print("开始爬虫程序.....")

    def process_item(self, item, spider):
        """
        中间数据过度处理
        :param item:
        :param spider:
        :return:
        """
        self.csv_write.writerow(dict(item))

        return item

    def close_spider(self, spider):
        """
        爬中结束调用
        :param spider:
        :return:
        """
        self.fp.close()

        print("爬虫结束.....")
