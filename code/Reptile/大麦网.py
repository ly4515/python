import requests
from lxml import etree
url = 'https://search.damai.cn/search.htm'
respose = requests.get(url).content.decode('utf-8')
html = etree.HTML(respose)
print(html)
lists = html.xpath('div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/a/@herf')
print(lists)
# /html/body/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/a
