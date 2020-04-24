import requests


def deal():
    """
    requests 使用代理
    :return: None
    """
    url = "http://httpbin.org/ip"

    proxy = {
        "http": "221.180.170.104:8080"
    }

    response = requests.get(url, proxies=proxy)

    print(response.text)


if __name__ == '__main__':
    deal()