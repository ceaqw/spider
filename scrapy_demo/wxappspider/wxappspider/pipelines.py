# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import csv


class WxappspiderPipeline(object):
    def __init__(self):
        fp = open("contrnt_wxapp.csv", "w", encoding="utf8", newline="")
        self.write = csv.DictWriter(fp, ["title", "author", "pub_time", "content"])
        self.write.writeheader()

    def process_item(self, item, spider):
        """
        过程数据处理
        :param item:
        :param spider:
        :return:
        """
        self.write.writerow(dict(item))
        return item
