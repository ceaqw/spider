# encoding: utf8
# descirbe: 解析电影天堂最新电影下载地址

from lxml import etree
import requests
from urllib import parse
import csv

def get_videos_url():
    """
    解析页面最新视频ftp下载地址
    :return:
    """
    url = 'http://www.dytt8.net'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    }
    csv_headers = ["name_zh", "name", "year", "produce_area", "type", "language", "language_print", "update", "score", "video_size", "file_size", "time", "director", "down_url"]

    movies = {}
    movies_csv = open("movies.csv", "w", encoding="utf8", newline="")
    csv_cursor = csv.DictWriter(movies_csv, csv_headers)
    csv_cursor.writeheader()

    response = requests.get(url, headers=headers)
    html = etree.HTML(response.content.decode("gbk"))

    movies_xpath = html.xpath("//div[@class='co_content2']//a")

    for movie in movies_xpath[1:]:
        resp_movie = requests.get(parse.urljoin(url, movie.xpath("./@href")[0]))
        movie_xpath = etree.HTML(resp_movie.content.decode("gbk"))
        detail_msg = movie_xpath.xpath("//div[@id='Zoom']//text()")

        for msg in detail_msg:
            if "◎" not in msg and "ftp" not in msg:
                continue

            if "◎译\u3000\u3000名" in msg:
                movies["name_zh"] = msg.split("\u3000")[-1]
            elif "◎片\u3000\u3000名" in msg:
                movies["name"] = msg.split("\u3000")[-1]
            elif "◎年\u3000\u3000代" in msg:
                movies["year"] = msg.split("\u3000")[-1]
            elif "◎产\u3000\u3000地" in msg:
                movies["produce_area"] = msg.split("\u3000")[-1]
            elif "◎类\u3000\u3000别" in msg:
                movies["type"] = msg.split("\u3000")[-1]
            elif "◎语\u3000\u3000言" in msg:
                movies["language"] = msg.split("\u3000")[-1]
            elif "◎字\u3000\u3000幕" in msg:
                movies["language_print"] = msg.split("\u3000")[-1]
            elif "◎上映日期" in msg:
                movies["update"] = msg.split("\u3000")[-1]
            elif "◎豆瓣评分" in msg:
                movies["score"] = msg.split("\u3000")[-1]
            elif "◎视频尺寸" in msg:
                movies["video_size"] = msg.split("\u3000")[-1]
            elif "◎文件大小" in msg:
                movies["file_size"] = msg.split("\u3000")[-1]
            elif "◎片\u3000\u3000长" in msg:
                movies["time"] = msg.split("\u3000")[-1]
            elif "◎导\u3000\u3000演" in msg:
                movies["director"] = msg.split("\u3000")[-1]
            elif "ftp" in msg:
                movies["down_url"] = msg

        print("当前进度： %d/%d" % (movies_xpath.index(movie), len(movies_xpath)))
        csv_cursor.writerow(movies)


if __name__ == '__main__':
    get_videos_url()