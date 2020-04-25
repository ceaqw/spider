# encoding: utf8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def deal():
    """
    页面等待操作
    :return: None
    """
    url = "https://www.baidu.com"

    # driver = webdriver.Chrome()
    # driver.get(url)

    # 显式等待
    # try:
    #     WebDriverWait(driver, 10).until(
    #         EC.title_contains("百度")
    #         # EC.presence_of_all_elements_located((By.ID, "kw"))
    #     )
    #     print("显示等待通过")
    # finally:
    #     driver.quit()

    # 隐式等待
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(url)
    print("隐式等待开始")
    try:
        driver.find_element_by_id("kwss")
    finally:
        driver.quit()
    print("隐式等待结束")


if __name__ == '__main__':
    deal()