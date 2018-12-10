
import requests
from lxml import etree
import json
from mongo_helper import *

url = 'https://www.qichamao.com/cert-wall'
headers = {
    'Referer': 'https://www.qichamao.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Host': 'www.qichamao.com'
}


def get_first_page():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


#第二页之后
def get_page(page):
    session = requests.Session()

    post_data = {
        'page':page,
        'pagesize':100
    }
    response = session.post(url, post_data, headers=headers)

    if response.status_code == 200:
        return response.text
    return None

#解析第一页
def parse_first_page(html):
    result_list = []
    etree_html = etree.HTML(html)
    lists_boxs = etree_html.xpath('//div[@class="firmwall_list_box"]')
    for item in lists_boxs:
        result_dict = {}
        company_name = item.xpath('.//h2[@class="firmwall_list_tit toe"]/a/text()')[0]
        result_dict['company_name'] = company_name
        contact_info = item.xpath('.//div[@class="firmwall_list_cinfo"]/text()')[0]
        result_dict['contact_info'] = contact_info
        contact_people = item.xpath('.//div[@class="firmwall_list_cinfo"]/text()')[1]
        result_dict['contact_people'] = contact_people
        email = item.xpath('.//div[@class="firmwall_list_cinfo"]/text()')
        if len(email) > 2:
            email = email[2]
        else:
            email = ''
        result_dict['email'] = email

        #插入mongodb
        insert_company(result_dict)

        result_list.append(result_dict)
    return result_list


#解析json数据
def parse_json(html):
    result_json = json.loads(html)
    print(len(result_json))
    data_list = result_json['dataList']
    result_list = []

    for item in data_list:
        result_dict = {}
        result_dict['company_name'] = item.get('CompanyName','')
        result_dict['contactor'] = item.get('c_name','')
        result_dict['contact_info'] = item.get('c_phone','')
        result_dict['email'] = item.get('c_email','')

        #插入mongodb
        insert_company(result_dict)

        result_list.append(result_dict)
    return result_list

def main():
    # html = get_page()
    # print(html)
    first_page = get_first_page()
    result_list = parse_first_page(first_page)

    page = 2
    while True:
        html = get_page(page)
        json_results = parse_json(html)
        if len(json_results) == 0:
            break
        print(json_results)
        print(len(json_results))
        page += 1


if __name__ == '__main__':
    main()