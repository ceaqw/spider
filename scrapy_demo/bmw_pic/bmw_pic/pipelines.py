# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
from urllib import request
# from pypinyin import pinyin, Style


class BmwPicPipeline(object):
    def __init__(self):
        self.path = os.path.join(os.path.dirname(__file__), "images")

        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def process_item(self, item, spider):
        # print(item["part_name"])
        part_name = item["part_name"]
        # part_name = "".join(["".join(i) for i in pinyin(part_name, style=Style.FIRST_LETTER)])
        urls = item["urls"]
        part_dir = os.path.join(self.path, part_name)

        if not os.path.exists(part_dir):
            os.mkdir(part_dir)

        for image_url in urls:
            image_name = image_url.split("__")[-1]
            request.urlretrieve(image_url, os.path.join(part_dir, image_name))

        return item