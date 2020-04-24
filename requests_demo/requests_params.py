import requests


def deal():
    """
    带参数、请求头请求
    :return: None
    """
    url = "https://www.baidu.com"

    params = {
        "wd": "你好"
    }
    headers = {
        'User-Agent': 'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    }

    response = requests.get(url, params=params, headers=headers, verify=True)

    print(response.text)

if __name__ == '__main__':
    deal()