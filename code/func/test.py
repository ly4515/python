import os
from requests.api import head
import xlsxwriter


path = 'D:/mine/Python/photo/'
filenames = os.listdir(path)
# 创建一个新的工作簿wb
wb = xlsxwriter.Workbook('D:/mine/Python/excel/photo.xlsx')
# 使用active获取创建工作簿wb时自动生成的sheet
sheet = wb.add_worksheet('photo')
url = 'jjijiji'
n = 1
for filename in filenames:
    sheet.write(n, 0, filename)
    sheet.write(n, 1, url)
    n = n+1

# 工作簿落盘
wb.close()
full_url = []
full = url + list
fu = full_url.append(full)
