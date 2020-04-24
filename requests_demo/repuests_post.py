import requests


def deal():
    """
    post请求方法
   :return: None
    """
    url = "https://fanyi.baidu.com/v2transapi?from=zh&to=en"

    data = {
        "from": "zh",
        "to": "en",
        "query": "你好",
        'simple_means_flag': '3',
        'sign': '232427.485594',        #特殊标记，暂时未分析出其来源
        "token": "65bf899513fea3ec78b02a857115e6cd"
    }

    headers = {
        'User-Agent': 'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        'origin': 'https://fanyi.baidu.com',
        'referer': 'https://fanyi.baidu.com/?aldtype=16047',
        'cookie': 'cookie: BIDUPSID=B66B5CA6CF7AEDB30C0484E436B12D31; PSTM=1577972421; BAIDUID=D693D7495CDBC16263CCF85869189199:FG=1; cflag=13%3A3; BDUSS=2E1WWpURzhrbzlwWTJrQjdZdGxsfnJnTUplN09rSkRuR0RkYmhJSTRoeElCcjFlRVFBQUFBJCQAAAAAAAAAAAEAAADM-y-eQ0VBUVdDQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEh5lV5IeZVeQ; H_PS_PSSID=; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1587708504; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1587708504; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __yjsv5_shitong=1.0_7_690e4151c7e7cd25ed96a1aa272fd46b2fed_300_1587708505173_1.193.183.42_8d10191b; yjs_js_security_passport=92cd30f4c2e6a84b0b0e69b09d08b1bc65f08c72_1587708505_js'
    }

    response = requests.post(url, data=data, headers=headers)

    print(response.json()["trans_result"]["data"][0]["dst"])


if __name__ == '__main__':
    deal()