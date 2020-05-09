# coding: utf8

import requests
import threading
import csv

from lxml import etree
from queue import Queue


class BSSpider(threading.Thread):
    """
    爬虫线程基类
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }

    def __init__(self, page_queue, joke_queue, *args, **kwargs):
        super(BSSpider, self).__init__(*args, **kwargs)

        self.base_domain = "http://www.budejie.com"
        self.page_queue = page_queue
        self.joke_queue = joke_queue

    def run(self) -> None:
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            resp = requests.get(url, headers=self.headers).text
            html = etree.HTML(resp)
            desc_list = html.xpath("//div[@class='j-r-list-c-desc']")
            for desc in desc_list:
                jokes = desc.xpath(".//text()")
                joke = "\n".join(jokes).strip()
                link = self.base_domain + desc.xpath(".//a/@href")[0]
                self.joke_queue.put((joke, link))
            print('=' * 30 + "第%s页下载完成！" % url.split('/')[-1] + "=" * 30)


class BSWrite(threading.Thread):
    """
    线程写入类
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }

    def __init__(self, joke_queue, writer, gLock, *args, **kwargs):
        super(BSWrite, self).__init__(*args, **kwargs)

        self.joke_queue = joke_queue
        self.writer = writer
        self.lock = gLock

    def run(self) -> None:
        while True:
            try:
                joke, link = self.joke_queue.get(timeout=30)
                self.lock.acquire()
                self.writer.writerow((joke, link))
                self.lock.release()
                print("保存一条")
            except Exception as e:
                print(e)
                break


if __name__ == '__main__':
    page_queue = Queue(10)
    joke_queue = Queue(500)
    gLock = threading.Lock()
    fp = open("bsbdj.csv", "a", newline="", encoding="utf8")
    writer = csv.writer(fp)
    writer.writerow(("joke", "link"))

    for i in range(1, 11):
        url = 'http://www.budejie.com/text/%d' % i
        page_queue.put(url)

    for i in range(5):
        t = BSSpider(page_queue, joke_queue)
        t.start()

    for i in range(5):
        t = BSWrite(joke_queue, writer, gLock)
        t.start()
