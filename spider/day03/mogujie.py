import requests
import json
import time
import random
from agent_helper import get_random_agent
import sqlalchemy_helper
from proxy_helper import get_proxies
def get_one_page(url,proxy):

	agent = get_random_agent()
	print(agent)
	headers =  {
		"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
	}
	# headers = {
	# 	'Referer': '[图片]https://www.qichamao.com/cert-wall/',
	# 	'User-Agent': agent,
	# 	'Host': '[图片]www.qichamao.com',
	# 	'Accept': 'application/json, text/plain, */*',
	# 	'Accept-Encoding': 'gzip, deflate, sdch',
	# 	'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,mt;q=0.2',
	# 	'Connection': 'keep-alive',
	# 	'X-Requested-With': 'XMLHttpRequest',
	# }
	response = None
	if proxy is None:
		response = requests.get(url, headers=headers)
	else:
		response = requests.get(url, headers=headers,proxies=proxy)
	if response.status_code == 200:
		text = response.content.decode('utf-8')
		return text
	return None

def parse_page(html):
	i = html.index('(')
	html = html[i+1:]
	html = html[:-2]
	# print(html)
	result_dict = json.loads(html)
	# print(result_dict)
	isEnd = result_dict['result']['wall']['isEnd']
	if isEnd:
		return None

	results = result_dict['result']['wall']['docs']
	result_list = []
	for item in results:
		mogu_dict = {}
		mogu_dict['tradeItemId'] = item.get('tradeItemId','')
		mogu_dict['tradeType'] = item.get('tradeType','')
		mogu_dict['img'] = item.get('img','')
		mogu_dict['clientUrl'] = item.get('clientUrl','')
		mogu_dict['link'] = item.get('link','')
		mogu_dict['itemMarks'] = item.get('itemMarks','')
		mogu_dict['acm'] = item.get('acm','')
		mogu_dict['title'] = item.get('title','')
		mogu_dict['cparam'] = item.get('cparam','')
		mogu_dict['orgPrice'] = item.get('orgPrice','')
		mogu_dict['hasSimilarity'] = item.get('hasSimilarity','')
		mogu_dict['sale'] = item.get('sale','')
		mogu_dict['cfav'] = item.get('cfav','')
		mogu_dict['price'] = item.get('price','')
		mogu_dict['similarityUrl'] = item.get('similarityUrl','')
		result_list.append(mogu_dict)
	return result_list

def save_json(result_list):
	json_text = json.dumps(result_list,ensure_ascii=False)
	with open('./mogu.json','a',encoding='utf-8') as f:
		f.write(json_text)


def main():
	page = 1
	# total_list = []
	while(True):
		url = 'https://list.mogujie.com/search?callback=jQuery21103620560807485016_1543376828343&_version=8193&ratio=3%3A4&cKey=15&page=' + str(page) + '&sort=pop&ad=0&fcid=50240&action=clothing&acm=3.mce.1_10_1jxby.128038.0.a1h6zraFaPO8z.pos_0-m_464803-sd_119&ptp=1.n5T00.0.0.RBCVgat7&_=1543376828434'
		# time.sleep(1)
		html = ''
		try:
			html = get_one_page(url)
		except Exception as e:
			html = ''
		if '(' not in html:
			print('.....in error......')

			proxy = get_proxies()
			print('....获取代理IP....')
			print(proxy)
			t = random.randint(1,3)
			time.sleep(t)
			continue

		# print(html)
		result_list = parse_page(html)
		# print(len(result_list))
		if result_list is None:
			break

		print(page,len(result_list))

		sqlalchemy_helper.save_db(result_list)

		# save_json(result_list)

		# total_list.extend(result_list)
		page += 1

if __name__ == '__main__':
    main()