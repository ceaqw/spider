# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv

from .settings import CITY_NAME

class PartjobPipeline(object):
    def __init__(self):
        super(PartjobPipeline, self).__init__()

        header = ["name", "job_time", "job_type", "salary", "pay_method", "address", "num", "job_detail", "salary_detail", "job_time_detail", "address_detail"]
        f = open(CITY_NAME+".csv", "a", encoding="utf8", newline="")
        self.writer = csv.DictWriter(f, header)
        self.writer.writeheader()

    def process_item(self, item, spider):
        """
        储存数据处理
        :param item:
        :param spider:
        :return:
        """
        self.writer.writerow(dict(item))
        return item
