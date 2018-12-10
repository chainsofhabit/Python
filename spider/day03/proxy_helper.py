import requests

def get_page():
    url = ""
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    }

    response = requests.get(url,headers=headers)

    if response.status_code == 200:
        return response.json()

def get_proxies():
    ip_json = get_page()
    ip = ip_json['msg'][0]['ip']
    port = ip_json['msg'][0]['port']
    proxy = ip + ':' + port
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    }
    return proxies