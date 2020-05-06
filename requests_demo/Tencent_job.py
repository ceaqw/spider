# coding: utf8
# describe: 腾讯招聘网爬虫, requests模拟发送get请求获取ajax加载的数据

import requests


def get_class_url():
    """
    获取类目的地址
    :return:
    """
    url = "https://careers.tencent.com/tencentcareer/api/post/ByHomeCategories?timestamp=1588474672171&num=6&language=zh-cn"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "cookie": "pgv_pvi=9760113664; _ga=GA1.2.1166311162.1578063723; _gcl_au=1.1.294868577.1586227694; loading=agree",
        "referer": "https://careers.tencent.com/",
    }
    data = {
        "timestamp": "1588474672171",
        "num": "6",
        "language": "zh-cn"
    }

    resp = requests.get(url, headers=headers, data=data)
    resp_data = resp.json()

    for category in resp_data["Data"]:
        categoryName = category["CategoryName"]
        categoryId = category["CategoryId"]
        job_list_page(categoryName, categoryId)


def job_list_page(categoryName, categoryId):
    """
    职位类目下的具体列表
    :param job_href:
    :return:
    """
    url = "https://careers.tencent.com/tencentcareer/api/post/Query"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "cookie": "pgv_pvi=9760113664; _ga=GA1.2.1166311162.1578063723; _gcl_au=1.1.294868577.1586227694; loading=agree",
        "referer": "https://careers.tencent.com/",
    }
    params = {
        "timestamp": "1588476060003",
        "parentCategoryId": categoryId,
        "pageIndex": "1",
        "pageSize": "10",
        "language": "zh-cn",
        "area": "cn"
    }

    resp = requests.get(url, params=params, headers=headers)
    print(resp.json())


if __name__ == '__main__':
    job_list_page("11","40001")
