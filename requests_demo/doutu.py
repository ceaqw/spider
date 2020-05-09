# coding: utf8
# describe: 斗图网爬虫

import requests
import threading
import os
import re

from urllib import request
from lxml import etree
from queue import Queue

HEADERS = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

class ParsePage(threading.Thread):
    def __init__(self, parse_queue, down_queue, *args, **kwargs):
        super(ParsePage, self).__init__(*args, **kwargs)

        self.parse_queue = parse_queue
        self.down_queue = down_queue

    def run(self):
        """
        运行页面解析
        :return:
        """
        while True:
            if self.parse_queue.empty():
                break
            url = self.parse_queue.get()
            resp = requests.get(url, headers=HEADERS).text
            html = etree.HTML(resp)
            imgs = html.xpath("//div[@class='page-content text-center']//a//img")
            for img in imgs:
                if img.get("class") == "gif":
                    continue
                img_url = img.xpath(".//@data-original")[0]
                alt = img.xpath(".//@alt")[0]
                alt = re.sub(r'[，。？?,/\\·]', '', alt)
                self.down_queue.put((img_url, alt))


class DownImg(threading.Thread):
    def __init__(self, down_queue, *args, **kwargs):
        super(DownImg, self).__init__(*args, **kwargs)

        self.down_queue = down_queue
        self.path = os.path.dirname(__file__) + "/images_doutu/"

    def run(self) -> None:
        """
        下载函数
        :return:
        """
        while True:
            try:
                img_url, alt = self.down_queue.get(timeout=30)
                suffix = os.path.splitext(img_url)[1]
                request.urlretrieve(img_url, self.path+alt+suffix)
                print(alt + suffix + "下载完成！")
            except:
                break


if __name__ == '__main__':

    parse_queue = Queue(10)
    down_queue = Queue(200)

    for i in range(1, 11):
        url = "http://www.doutula.com/photo/list/?page=%d" % i
        parse_queue.put(url)

    for i in range(5):
        t = ParsePage(parse_queue, down_queue)
        t.start()

    for i in range(10):
        t = DownImg(down_queue)
        t.start()


