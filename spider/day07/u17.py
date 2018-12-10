import requests
from lxml import etree
import json
from mongo_helper import *
url = 'http://www.u17.com/comic/ajax.php?mod=comic_list&act=comic_list_new_fun&a=get_comic_list'
headers = {
    'Referer': 'http://www.u17.com/comic_list/th99_gr99_ca99_ss99_ob0_ac0_as0_wm0_co99_ct99_p1.html?order=2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Host': 'www.u17.com'
}

def get_first_page():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None



def get_page(page):
    session = requests.Session()
    post_data = {'data[page_num]': page,'data[order]':2,
                 'data[group_id]': 'no','data[accredit]': 'no',
                 'data[color]': 'no','data[comic_type]': 'no',
                 'data[series_status]': 'no','data[theme_id]':'no',
                 'data[read_mode]': 'no','data[is_vip]': 'no'}

    response = session.post(url, post_data, headers=headers)
    if response.status_code == 200:
        return response.text
    return None
def get_resource(url):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    }

    response = requests.get(url,headers=headers)

    if response.status_code == 200:
        return response.content
    return None

def write_images(url):
    file_name = url.split('/')[-1]
    print(url)
    content = get_resource(url)
    with open('./image/%s' % file_name,'wb') as f:
        f.write(content)

def parse_json(html):
    result_json = json.loads(html)
    data_list = result_json['comic_list']
    result_list = []
    for item in data_list:
        result_dict = {}
        result_dict['id'] = item.get('comic_id','')
        result_dict['name'] = item.get('name','')

        result_dict['cover'] = item.get('cover','')
        url = result_dict['cover']
        # write_images(url)

        result_dict['update_type'] = item.get('update_type','')
        result_dict['line1'] = item.get('line1','')
        result_dict['line2'] = item.get('line2','')

        insert_comic(result_dict)

        result_list.append(result_dict)
    return result_list


def main():
    # first_page = get_first_page()

    page = 1
    while True:
        print(page)
        html = get_page(page)
        print(html)
        json_results = parse_json(html)
        if len(json_results) == 0:
            break
        print(json_results)
        print(len(json_results))
        page += 1


if __name__ == '__main__':
    main()