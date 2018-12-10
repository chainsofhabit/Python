from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from lxml import etree
import time

import jd_db_helper

chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.set_window_size(1400, 700)
wait = WebDriverWait(browser, 5)

def get_page(page):
    if page == 1:
        url = 'https://www.jd.com'
        browser.get(url)

        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#key')))
        input.clear()
        input.send_keys('羽毛球拍')

        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#search button.button')))
        submit.click()
        time.sleep(3)
        # print(browser.current_url)
    if page > 1:
        #填入页码编号
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage input.input-txt')))
        input.clear()
        input.send_keys(page)
        #点击下一页
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_bottomPage .btn.btn-default')))
        submit.click()


    for i in range(16):
        str_js = 'var step = document.body.scrollHeight / 16; window.scrollTo(0, step * %d)' % (i + 1)
        browser.execute_script(str_js)
        time.sleep(3)

    return browser.page_source


def parse_page(page_source):
    html_etree = etree.HTML(page_source)
    result_list = html_etree.xpath('//div[@id="J_goodsList"]//ul[@class="gl-warp clearfix"]/li[@class="gl-item"]')
    # result_list = html_etree.xpath('//div[@id="J_goodsList"]')
    spider_list = []
    db = jd_db_helper.get_db_connection()
    cursor = jd_db_helper.get_cursor(db)
    for item in result_list:
        result_dict = {}
        result_dict['sku'] = item.xpath('./@data-sku')[0]
        result_dict['name'] = item.xpath('.//div[@class="p-name p-name-type-2"]//em/text()')[0]
        result_dict['price'] = item.xpath('.//div[@class="p-price"]//i/text()')[0]
        result_dict['href'] = item.xpath('.//div[@class="p-img"]/a/@href')[0]
        img = item.xpath('.//div[@class="p-img"]//img/@src')
        if len(img):
            result_dict['img'] = img[0]
        else:
            result_dict['img'] = ''
        # comment = item.xpath('.//div[@class="p-comm"]/span/text()')
        # if len(comment):
        #     result_dict['comment'] = comment[0]
        # else:
        #     result_dict['comment'] = ''
        jd_db_helper.insert_record(db, cursor, result_dict)

        spider_list.append(result_dict)

        # 关闭数据库
    jd_db_helper.close_connection(db)
    return spider_list
    # print(spider_list)

def main():
    for page in range(50):
        print(page)
        print("*" * 20)
        html = get_page(page + 1)
        parse_page(html)


if __name__ == '__main__':
    main()
