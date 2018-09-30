import requests

url = "https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2808438283,4249462766&fm=26&gp=0.jpg"
response = requests.get(url)
with open("./files/load.jpg","wb")as f:
    f.write(response.content)