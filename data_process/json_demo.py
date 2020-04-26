# encoding: utf8
# describe: json文件的读取与写入

import json


data_json = [
    {
        'username': "张三",
        'age': 18,
        'country': 'china'
    },
    {
        'username': '李赛',
        'age': 20,
        'country': 'china'
    }
]

def deal():
    """
    json数据解析处理
    :return:
    """
    # json到字符串
    json_str = json.dumps(data_json)
    print(json_str)
    print(type(json_str))

    # 字符串到json
    json_data = json.loads(json_str)
    print(json_data)
    print(type(json_data))

    # json写入文件
    with open("data.json", "w", encoding="utf8") as fp:
        json.dump(data_json, fp, ensure_ascii=False)

    # json文件读取
    with open("data.json", "r", encoding="utf8") as fp:
        read_data = json.load(fp)
        print(read_data)
        print(type(read_data))


if __name__ == '__main__':
    deal()