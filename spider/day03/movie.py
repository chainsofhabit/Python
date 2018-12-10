import requests
import re
from agent_helper import get_random_agent

url = 'https://www.mkv99.com/vod-detail-id-9462.html'


def get_one_page(url):
    agent = get_random_agent()
    headers = {
		"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
	}

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        text = response.content.decode('utf-8')
        return text
    return None

def parse_page(html):
    pattern = re.compile('downurls="第.*?集(.*?)/#"',re.S)
    href = re.findall(pattern,html)

    return href

def main():
    html = get_one_page(url)
    result_list = parse_page(html)
    print(result_list)

if __name__ == '__main__':
    main()