# encoding: utf8

import requests
import urllib
import urllib.parse


def getData(city_quote):
    """
    通过post请求解析拉勾网对应城市的json数据集
    :param city_quote:
    :return:
    """
    url = "https://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionalRes".format(city_quote)

    headers = {
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": "user_trace_token=20200301114810-40556cbd-ac17-4854-ae50-e5aacdaa9aab; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217094356904f1-0fb4889adf6cd1-4313f6b-2073600-17094356905660%22%2C%22%24device_id%22%3A%2217094356904f1-0fb4889adf6cd1-4313f6b-2073600-17094356905660%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _ga=GA1.2.1282471430.1583034493; LGUID=20200301114811-928d49c2-4465-439a-a16c-cef8b834998e; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAABAGABFA87D814047DE2D9143FD964F13B5CF011; WEBTJ-ID=04252020%2C131057-171afbeee7a243-0ec1918b465381-7373667-2073600-171afbeee7c720; _gid=GA1.2.1088974098.1587791458; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1586235118,1586925135,1587791458; X_MIDDLE_TOKEN=24ef3fd0e84859d0a3e459bed747ee45; X_HTTP_TOKEN=bdbd8729e637bc9f38740878512e3fbecc22034874; _gat=1; PRE_UTM=; PRE_HOST=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGSID=20200425165304-fee9bb75-b8ee-4185-a4ba-bf572108bdba; PRE_SITE=; TG-TRACK-CODE=index_search; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1587804804; LGRID=20200425165323-082cddcd-7423-4062-ab39-0b278dc1013e; SEARCH_ID=87417fff66354d1b9447aaaf07b17309",
        "origin": "https://www.lagou.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
        "referer": "https://www.lagou.com/jobs/list_{}?labelWords=&fromSearch=true&suginput=".format(city_quote),
    }
    data = {
        "first": "true",
        "pn": "1",
    }

    response = requests.post(url, data=data, headers=headers)
    result = response.json()["content"]["hrInfoMap"]
    for i in result:
        print(result[i])


def deal():
    """
    解析对应城市数据
    :return:
    """
    city_quote = urllib.parse.quote("郑州")
    getData(city_quote)


if __name__ == '__main__':
    deal()