from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from lxml import etree
from urllib import parse
import requests

chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.set_window_size(1400, 700)
wait = WebDriverWait(browser, 5)



def get_page():
    url = 'https://www.xiami.com/chart?spm=a1z1s.6843761.1110925385.2.DzUm9P'

    browser.get(url)
    # print(browser.page_source)
    return browser.page_source

def get_resource(url):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    }

    response = requests.get(url,headers=headers)

    if response.status_code == 200:
        return response.content
    return None

def parse_page(html):
    html_etree = etree.HTML(html)
    result_list = html_etree.xpath('//div[@id="body"]//div[@id="chart"]//tr')

    for item in result_list:
        s = item.xpath('./@data-mp3')[0]
        music = str2url(s)
        print(music)
        content = get_resource(music)
        file_name = music.split('/')[-1].split('?')[0]
        with open('./xiami_music/%s' % file_name,'wb') as f:
            f.write(content)




def str2url(s):
    # s = '9hFaF2FF%_Et%m4F4%538t2i%795E%3pF.265E85.%fnF9742Em33e162_36pA.t6661983%x%6%%74%2i2%22735'
    num_loc = s.find('h')
    rows = int(s[0:num_loc])
    strlen = len(s) - num_loc
    cols = int(strlen / rows)
    right_rows = strlen % rows
    new_s = list(s[num_loc:])
    output = ''
    for i in range(len(new_s)):
        x = i % rows
        y = i / rows
        p = 0
        if x <= right_rows:
            p = x * (cols + 1) + y
        else:
            p = right_rows * (cols + 1) + (x - right_rows) * cols + y
        output += new_s[int(p)]
    return parse.unquote(output).replace('^', '0')

def main():
    html = get_page()
    parse_page(html)

if __name__ == '__main__':
    main()
