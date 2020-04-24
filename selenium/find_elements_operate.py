# encoding: utf8

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ChromeOptions


def deal():
    """
    抓取页面元素
    :return: None
    """
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com/")

    # 直接寻找
    # input_tag = driver.find_element(By.CLASS_NAME, "s_ipt")
    # input_tag.send_keys("你好，世界！！")
    # input_tag.send_keys(Keys.ENTER)

    # 通过By查找
    # input_tag = driver.find_element(By.CLASS_NAME, "s_ipt")
    # input_tag.send_keys("你好，世界！！")
    # time.sleep(2)
    # input_tag.clear()
    # input_tag.send_keys("hello")
    # time.sleep(2)
    # input_tag.send_keys(Keys.ENTER)

    # 点击操作
    # input_tag = driver.find_element(By.CLASS_NAME, "s_ipt")
    # input_tag.send_keys("你好，世界！！")
    # time.sleep(2)
    # enter_btn = driver.find_element_by_id("su")
    # enter_btn.click()

    # 获取标签内容（建议xpath,使用lxml）
    submit_text = driver.find_elements_by_class_name("mnav")
    print("获取标签文本内容","-"*15)
    for i in submit_text:
        print(i.text)
    print("-"*30)

    # 保存加载的视图
    driver.save_screenshot("screen.png")
    # 获取标题
    print("加载的标题：", driver.title)
    # 获取cookie
    print("cookie", driver.get_cookie("domain"))
    print("cookies:", driver.get_cookies())
    # 删除cookie
    driver.delete_cookie("domain")
    driver.delete_all_cookies()
    # 获取当前页面url
    print("current url", driver.current_url)

    # 关闭当前加载的页面
    # driver.close()

    # 鼠标链动作
    # 鼠标移动到ac位置
    driver.find_element_by_id("kw").send_keys("你好")
    ac = driver.find_element_by_id("su")
    # 获取元素属性
    print("获取元素属性：", ac.get_attribute("id"))
    time.sleep(1)
    action = ActionChains(driver)
    # 移动鼠标
    action.move_to_element(ac)
    # 鼠标点击
    action.click()
    action.perform()
    # 双击鼠标
    # ActionChains(driver).move_to_element(ac).double_click().perform()
    # # 右击
    # ActionChains(driver).move_to_element(ac).context_click().perform()
    # # 单机&hold
    # ActionChains(driver).move_to_element(ac).click_and_hold().perform()
    # 两元素之间拖拽
    # ActionChains(driver).drag_and_drop(element01, element02).perform()
    # 从元素开始偏移量
    # ActionChains(driver).drag_and_drop_by_offset(element_start, xoffset=10, yoffset=10).perform()

    # Select 选择下拉列表框元素
    # 定位下拉列表元素
    # select = Select(select_element)
    # 选择第二个
    # select.select_by_index(1)
    # select.select_by_value("selected value")
    # select.select_by_visible_text("selected text")
    # 取消全选
    # select.deselect_all()

    # # 前进后退
    # driver.forward()
    # driver.back()
    #
    # # 窗口切换
    # for handle in driver.window_handles:
    #     driver.switch_to_window(handle)

    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    deal()