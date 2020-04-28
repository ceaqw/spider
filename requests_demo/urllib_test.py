# encoding: utf8

from urllib import request
from urllib import parse

url = "http://www.baidu.com"

response = request.urlopen(url)
# print(response.read().decode())

data = {"wd": "你好"}

url += "/s?"+parse.urlencode(data)
print(url)

response = request.urlopen(url)
print(response.read().decode())

# 保存网页数据至本地
request.urlretrieve(url, "hello_baidu.html")
