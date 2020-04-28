# encoding: utf8
# describe: 图形验证码的识别测试

from base64 import b64encode
import requests
import io

def captcha_recognizer():
    """
    识别图形验证码
    :return:
    """
    captcha_url = "https://marketplace-res-cbc-cn.obs.myhwclouds.com/app/logo/20181009/98dea972-8855-4348-9ef4-92bafb247ea4/1810091217084675.jpg"
    recognizer_url = "https://302307.market.alicloudapi.com/ocr/captcha"

    appcode = '28af21d76db548aba5d2f735a0c32e91'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Authorization': 'APPCODE ' + appcode
    }

    captcha = io.BytesIO(requests.get(captcha_url).content)
    recognizer_data = {
        "image": b64encode(captcha.read()),
        "type": 1001
    }

    captcha.close()

    response = requests.post(recognizer_url, data=recognizer_data, headers=headers)

    print(response.json())
    print("识别结果： ", response.json()["data"]["captcha"])


if __name__ == '__main__':
    captcha_recognizer()