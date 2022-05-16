#  纯文本文件 number.txt,将内容写到 numbers.xls 文件中
import json

text = 'D:/mine/Python/python/code/shiLi/number.txt'
with open(text, 'r', encoding='utf-8') as f:
    num = json.load(f)
    for lists in num:
        print(lists)
