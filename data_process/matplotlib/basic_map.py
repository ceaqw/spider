# coding: utf8

from matplotlib import pyplot as plt
import numpy as np


def bar_demo1():
    """
    堆叠柱状图
    :return:
    """
    y1 = (20, 35, 30, 35, 27)
    y2 = (25, 32, 34, 20, 25)

    p1 = plt.bar(range(5), y1, width=0.5, color="g", yerr=[3, 5, 2, 3, 3])
    p2 = plt.bar(range(5), y2, width=0.5, bottom=y1, color="r")

    plt.ylabel("age")
    plt.title("people age")
    plt.xticks(range(5), ["peo1", "peo2", "peo3", "peo4", "peo5"])

    plt.legend((p1[0], p2[0]), ("Men", "Women"))
    plt.show()


def lines_demo1():
    """
    线图
    :return:
    """
    pass


if __name__ == '__main__':
    bar_demo1()
