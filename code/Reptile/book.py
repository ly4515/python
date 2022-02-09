import requests
import re
import os

start_url = 'https://www.kanunu8.com/book3/6879/'
html = requests.get(start_url).content.decode('GB2312')


toc_block = re.findall('正文(.*?)</tbody>', html, re.S)[0]
toc_url = re.findall('href="(.*?)"', toc_block, re.S)

for url in toc_url:
    new_url = start_url+url
    html_p = requests.get(new_url).content.decode('GB2312')

    chapter_name = re.search('size="4">(.*?)<', html_p, re.S).group(1)
    text_block = re.search('<p>(.*?)</p>', html_p, re.S).group(1)
    text_block = text_block.replace('<br />', '')
    os.makedirs('D:/mine/Python/动物农场', exist_ok=True)
    with open(os.path.join('D:/mine/Python/动物农场', chapter_name+'.txt'), 'w', encoding='utf-8') as f:
        f.write(text_block)
