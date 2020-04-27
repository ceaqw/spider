# encoding: utf8
# describe: xapth语法的使用示例

from lxml import etree


def deal():
    """
    xpath 语法示例
    :return:
    """

    # 1. 获取所有tr标签
    # //tr
    # xpath函数返回的是一个列表
    # trs = html.xpath("//tr")
    # for tr in trs:
    #     print(etree.tostring(tr,encoding='utf-8').decode("utf-8"))

    # 2. 获取第2个tr标签
    # tr = html.xpath("//tr[2]")[0]
    # print(etree.tostring(tr,encoding='utf-8').decode("utf-8"))

    # 3. 获取所有class等于even的tr标签
    # trs = html.xpath("//tr[@class='even']")
    # for tr in trs:
    #     print(etree.tostring(tr,encoding='utf-8').decode("utf-8"))

    # 4. 获取所有a标签的href属性
    # aList = html.xpath("//a/@href")
    # for a in aList:
    #     print("http://hr.tencent.com/"+a)

    parser = etree.HTMLParser(encoding="utf8")
    html = etree.parse("tencent.html", parser=parser)

    job_name = html.xpath("//td[contains(@class, 'square')]//text()")
    print(job_name)
    job_type = html.xpath("//td[contains(@class, 'square')]/../td[2]/text()")
    print(job_type)


if __name__ == '__main__':
    deal()