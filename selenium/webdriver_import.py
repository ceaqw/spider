# encoding: utf8

from selenium import webdriver


def deal():
    """
    webdriver相关设置
    :return: None
    """
    url = "https://www.baidu.com"
    # driver_path = r"your driver's path"
    # driver = webdriver.Chrome(executable_path=driver_path)
    driver = webdriver.Chrome()
    driver.get(url)

    print(driver.page_source)
    driver.quit()

if __name__ == '__main__':
    deal()