# encoding: utf8
# describe: re解析requests返回的数据

import re
import requests

HEADERS = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }

def poem():
    """
    正则提取当前加载的页面的诗词
    :return:
    """
    url = "http://www.gushiwen.org/default_1.aspx"

    response = requests.get(url, headers=HEADERS).text
    title_list = re.findall(r'<div class="cont">.*?<b>(.*?)</b>', response, re.S)
    print(title_list)
    author_list = re.findall(r'<p class="source">.*?<a.*?><a.*?>(.*?)</a>', response, re.S)
    print(author_list)
    content_list = re.findall(r'<div class="contson" .*?>(.*?)</div>', response, re.S)
    content_list = [re.sub(r"<br />|\n", "", i, re.S) for i in content_list]
    print(content_list)


def joke():
    """
    搞笑段子抓取
    :return:
    """
    url = "https://www.qiushibaike.com/text/page/1/"
    response = requests.get(url, headers=HEADERS).text
    jokes_list = re.findall(r'<div class="content">.*?<span>(.*?)</span>', response, re.S)
    jokes_list = [re.sub(r"<.*?>", "", i) for i in jokes_list]
    for i in jokes_list:
        print(i)


if __name__ == '__main__':
    joke()