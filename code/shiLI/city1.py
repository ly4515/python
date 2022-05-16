import json
import xlwings
import os

city_file = 'D:/mine/Python/python/code/shiLi/city.txt'
excel_file = 'city.xls'

app = xlwings.App(visible=False, add_book=False)
if not os.path.exists(excel_file):
    # 新建excel
    excel = app.books.add()
    excel.save(excel_file)
wb = app.books.open(excel_file)
wb.sheets.add('city')
sheet = wb.sheets('city')

with open(city_file, 'r', encoding='utf-8') as f:
    # load:把文件打开，并把字符串变换为数据类型
    file = json.load(f)
    n = 1
    key = list(file.keys())
    for k in key:
        sheet.range('A'+str(n)).value = k
        n += 1
    value = list(file.values())
    n = 1
    for v in value:
        sheet.range('B'+str(n)).value = v
        n += 1

wb.save('city.xls')
app.quit()
