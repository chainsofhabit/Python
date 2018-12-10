import requests
from lxml import etree
import json
def get_resource(url):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    }

    response = requests.get(url,headers=headers)

    if response.status_code == 200:
        return response.content
    return None

#抓取HTML页面
def get_one_page(url):

	headers =  {
		"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
	}
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		text = response.content.decode('utf-8')
		return text
	return None

#解析页面
def parse_with_xpath(html):
	result_list = []
	etree_html = etree.HTML(html)
	result_channel = etree_html.xpath('//div[@class="channel-item"]')
	for channel in result_channel:
		result_dict = {}
		title = channel.xpath('./div[@class="bd"]/h3/a/text()')[0]
		like = channel.xpath('./div[@class="likes"]/text()')[0]
		href = channel.xpath('./div[@class="bd"]/h3/a/@href')[0]
		images = channel.xpath('./div[@class="bd"]//div[@class="pic-wrap"]/img/@src')
		content = channel.xpath('./div[@class="bd"]//div[@class="block"]/p/text()')[0]
		team = channel.xpath('./div[@class="bd"]//div[@class="source"]/span/a/text()')[0]
		time = channel.xpath('./div[@class="bd"]//div[@class="source"]/span[@class="pubtime"]/text()')[0]

		result_dict['title'] = title
		result_dict['like'] = like
		result_dict['href'] = href
		if len(images):
			result_dict['images'] = images[0]
		else:
			result_dict['images'] = ''
		result_dict['content'] = content
		result_dict['team'] = team
		result_dict['time'] = time
		result_list.append(result_dict)
	return result_list
	# print(result_list)

def write_image_files(result_list):
	for item in result_list:
		images_url = item['images']
		if len(images_url):
			file_name = images_url.split('/')[-1]
			content = get_resource(images_url)
			with open('./images/%s' % file_name,'wb') as f:
				f.write(content)
		else:
			continue

#取所有的页
def get_all_pages():
	result_list = []
	for i in range(10):
		page = i * 30
		if page == 0:
			url = 'https://www.douban.com/group/explore'
		else:
			url = 'https://www.douban.com/group/explore?start=' + str(page)
		html = get_one_page(url)

		one_page_result = parse_with_xpath(html)
		result_list += one_page_result
	return result_list


def save_json(result_list):
	json_text = json.dumps(result_list,ensure_ascii=False)
	with open('./douban.json','w',encoding='utf-8') as f:
		f.write(json_text)

def main():
	# html = get_one_page()
	# parse_with_xpath(html)
	result_list = get_all_pages()
	print(result_list)
	write_image_files(result_list)
	save_json(result_list)

if __name__ == '__main__':
    main()