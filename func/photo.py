import requests
from lxml import etree
import time

url = 'https://pic.netbian.com/'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3880.400 QQBrowser/10.8.4554.400'
}
rep = requests.get(url, headers=header)   # 请求网页
text = rep.text            # 获取网页的全部源代码
# etree.HTML()可以用来解析字符串格式的HTML文档对象，将传进去的字符串转变成_Element对象。
html = etree.HTML(text)
# 作为_Element对象，可以方便的使用getparent()、remove()、xpath()等方法。
lists = html.xpath('//div[@class="slist"]/ul/li/a/span/img/@src')

for list in lists:
    full_url = url + list
    re = requests.get(full_url)
    with open('D:/mine/Python/photo/+%s.jpg' % time.time(), 'wb') as f:
        f.write(re.content)   # 用content属性获得bytes对象，二进制数据
