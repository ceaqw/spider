# encoding: utf8
# describe: 抓取拉勾网下python栏目的数据

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from lxml import etree
import csv, time


class MySpider(object):
    """
    lagou网python栏目下数据抓取
    """

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.fp = open("lagou.csv", "a", encoding="utf8", newline="")
        self.writer = csv.DictWriter(self.fp, ['title', 'salary', 'city', 'work_years', 'education', "company_website", 'describe', 'acquire'])
        self.writer.writeheader()

    def run(self):
        """
        爬虫运行函数
        :return:
        """
        url = "https://www.lagou.com/jobs/list_python"
        self.driver.get(url)

        i = 0
        while True:
            i += 1
            print("正在进行第%d页的抓取" % i)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, """//span[contains(@class, "pager_next")]"""))
            )
            resources = self.driver.page_source
            self.parse_page(resources)
            next_page_btn = self.driver.find_element(By.XPATH, """//span[contains(@class, "pager_next")]""")
            if "pager_next_disabled" in next_page_btn.get_attribute("class"):
                break
            ActionChains(self.driver).click(next_page_btn).perform()
            time.sleep(1)

    def parse_page(self, resources):
        """
        页面解析函数
        :param resources:
        :return:
        """
        xpath_html = etree.HTML(resources)
        company_list = xpath_html.xpath("""//a[@class="position_link"]/@href""")
        for company_url in company_list:
            print(company_url)
            self.parse_company(company_url)
            time.sleep(1)

    def parse_company(self, company_url):
        """
        解析对应的企业的详细信息
        ['title', 'salary', 'city', 'work_years', 'education', "company_website", 'describe', 'acquire']
        :param company_url:
        :return:
        """
        self.driver.execute_script("""window.open("%s")""" % company_url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, """//dd[@class='job_bt']"""))
        )
        resource = self.driver.page_source
        xpath_html = etree.HTML(resource)
        title = xpath_html.xpath("""//h1[@class="name"]/text()""")[0]
        salary = xpath_html.xpath("""//dd[@class="job_request"]//span[1]/text()""")[0]
        city = xpath_html.xpath("""//dd[@class="job_request"]//span[2]/text()""")[0].replace("/", "").strip()
        work_years = xpath_html.xpath("""//dd[@class="job_request"]//span[3]/text()""")[0].replace("/", "").strip()
        education = xpath_html.xpath("""//dd[@class="job_request"]//span[4]/text()""")[0].replace("/", "").strip()
        company_website = xpath_html.xpath("""//*[@id="job_company"]//ul//a/@href""")[0]
        describe = "".join(xpath_html.xpath("""//div[@class="job-detail"]//text()"""))
        acquire = " ".join(xpath_html.xpath("""//li[@class="labels"]/text()"""))

        company_dict = {
            "title": title,
            "salary": salary,
            "city": city,
            "work_years": work_years,
            "education": education,
            "company_website": company_website,
            "describe": describe,
            "acquire": acquire
        }
        self.writor(company_dict)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def writor(self, company_dict):
        """
        保存每个公司的详细信息至csv文件
        :param company_dict:
        :return:
        """
        self.writer.writerow(company_dict)


if __name__ == '__main__':
    spider = MySpider()
    spider.run()