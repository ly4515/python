#  纯文本文件 city.txt为城市信息,将内容写到 city.xls 文件

import xlwt
import re

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('city')
reg = re.compile('"(\d+)" : "(.*?)"')
count = 0
with open('D:/mine/Python/python/code/shiLi/city.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    s = reg.findall(content)
    print(s)
    for i in s:
        worksheet.write(count, 0, label=i[0])
        worksheet.write(count, 1, label=i[1])
        count += 1

workbook.save('city.xls')
