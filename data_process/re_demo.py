# encoding: utf8
# describe: 正则表达式的应用

import re


def deal():
    """
    正则表达式的应用
    :return:
    """
    # 匹配单个字符
    text = "hello"
    ret = re.match(r"he", text)
    print("单字符匹配结果:", ret.group())

    text = "hel\tlo"
    ret = re.findall(r"\S", text)
    print("非空字符匹配:", ret)

    # []组合匹配
    ret = re.match(r"[\s\w]*", text)
    print("[]组合匹配结果:", ret.group())

    # 数字匹配
    text = "123hello"
    ret = re.match(r"\d+", text)
    print("数字匹配结果:", ret.group())

    # ()组匹配
    text = "hello123"
    ret = re.match(r".*(\d+)", text)
    print("()组匹配结果：", ret.group())
    print("()组匹配结果：", ret.groups())
    print("()组匹配结果：", ret.group(1))
    # 贪婪匹配问题
    ret = re.match(r".*?(\d+)", text)
    print("()组匹配结果：", ret.group())
    print("()组匹配结果：", ret.groups())
    print("()组匹配结果：", ret.group(1))

    # 电话号码匹配
    test_str = "12578900980"
    ret = re.match(r"1[34578]\d{9}", test_str)
    try:
        ret.group()
        print(test_str, "合法的电话号码")
    except:
        print(test_str, "不是合法的电话号码")

    # 验证邮箱
    email = "ceaqw@qqcom"
    ret = re.match(r"\w+@[0-9a-z]+\.[a-z]+", email)
    try:
        ret.group()
        print("合法的邮箱", email)
    except Exception as e:
        print(e, "不合法的邮箱", email)

    # 16. 验证URL
    text = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    ret = re.match(r"(http|https|ftp)://[^\s]+", text)
    print(ret.group())

    # 17. 验证身份证：
    text = "31131118908123230a"
    ret = re.match(r"\d{17}[\dxX]", text)
    # print(ret.group())

    # 18. ^（脱字号）：
    text = "hello"
    ret = re.search('^h', text)
    print("^（脱字号）：", ret.group())

    # 19. $：表示以...结尾：
    text = "xxx@163.com"
    ret = re.match(r"\w+@163.com$", text)
    print(ret.group())

    # 20. |：匹配多个字符串或者表达式：
    text = "https"
    ret = re.match(r"(ftp|http|https)$", text)
    print(ret.group())

    # 21：贪婪模式与非贪婪模式：
    text = "0123456"
    ret = re.match('\d+?',text)
    print(ret.group())

    # text = "<h1>标题</h1>"
    ret = re.match('<.+?>',text)
    print(ret.group())

    # 22：匹配0-100之间的数字
    # 可以出现的：1，2，3，10，100，99
    # 有三种情况：1，99，100
    # 不可以出现的：09，101


if __name__ == '__main__':
    deal()