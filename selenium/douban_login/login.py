# coding: utf8
# describe: 使用selenium操作浏览器模拟登录豆瓣

import time
import numpy as np

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def doubanLogin():
    """
    模拟登陆豆瓣
    :return: None
    """
    url = "https://accounts.douban.com/passport/login"
    login_name = "17737962591"
    login_pass = "151437chen"

    options = webdriver.ChromeOptions()
    options.add_argument('User-Agent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"')

    driver = webdriver.Chrome(options=options)

    driver.get(url)
    driver.find_element(By.CLASS_NAME, "account-tab-account").click()
    driver.find_element(By.ID, "username").send_keys(login_name)
    driver.find_element(By.ID, "password").send_keys(login_pass)

    driver.find_element(By.CLASS_NAME, "btn-account").click()

    if driver.current_url == "https://accounts.douban.com/passport/login":
        time.sleep(1)
        driver.switch_to.frame(0)
        try:
            draped_element = driver.find_element(By.XPATH, '//img[@id="slideBlock"]')
            print("开始拖拽")
            # 拖拽
            track_list = np.random.rand(5)
            ratio = 220/sum(track_list)
            track_list = [int(i*ratio) for i in track_list]

            for i in track_list:
                ActionChains(driver).click_and_hold(draped_element).move_by_offset(xoffset=i, yoffset=0).perform()
                time.sleep(0.3)
            ActionChains(driver).release().perform()
        except Exception as e:
            print(e)

    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    doubanLogin()
