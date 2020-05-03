# coding: utf8

import requests
import json

from lxml import etree


class ProxyGet(object):
    """
    ipNum: 获取的代理数量
    prixyProtocol: 代理类型 -> http,https
    """
    url_list = ["http://www.xiladaili.com/gaoni/" + str(i) for i in range(1, 100)]
    verify_url = "://httpbin.org/ip"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
    }

    def __init__(self, ipNum, proxyProtocol):
        self.ip_list = []
        if ipNum > 50:
            ipNum = 50
        self.ip_num = ipNum
        self.proxy_protocol = proxyProtocol

    def proxy_ip_get(self):
        """
        获取可用的代理ip
        :return:
        """
        while True:
            for url in ProxyGet.url_list:
                response = requests.get(url, headers=ProxyGet.headers)

                html = etree.HTML(response.text)

                ip_list = html.xpath("//tr//td[1]/text()")

                for i in ip_list:
                    if len(self.ip_list) >= self.ip_num:
                        return
                    proxy = {
                        self.proxy_protocol: i
                    }
                    try:
                        resp = requests.get(self.proxy_protocol + ProxyGet.verify_url, proxies=proxy)
                        resp_json = json.loads(resp.text)
                        if resp_json["origin"] == i.split(":")[0]:
                            if i not in self.ip_list:
                                self.ip_list.append(i)
                                yield i
                    except:
                        pass


if __name__ == '__main__':
    # 声明类，传入参数即要获得的代理数量，程序自动检验代理的可用性
    # 设置了上限50个
    # 以迭代器的方式返回高速响应的http,https代理，遍历即可获取
    getIp = ProxyGet(5, "http")
    for i in getIp.proxy_ip_get():
        print("可用代理:", i)