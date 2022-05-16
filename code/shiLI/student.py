# 纯文本文件 student.txt为学生信息，将内容写到 student.xls 文件中

import xlwings
import os
import json

stu_file = 'D:/mine/Python/python/code/shiLi/student.txt'
ex_file = 'student.xls'

app = xlwings.App(visible=True, add_book=False)
if not os.path.exists(ex_file):
    excel = app.books.add()
    excel.save(ex_file)
workbook = app.books.open(ex_file)
workbook.sheets.add('student')
sheet = workbook.sheets('student')


def write():
    with open(stu_file, 'r', encoding='utf-8') as f:
        info = json.load(f)
        key = list(info.keys())
        cow = 1
        for k in key:
            sheet.range('A' + str(cow)).value = k
            cow += 1
        values = list(info.values())
        cow = 1
        for value in values:
            sheet.range('B' + str(cow)).value = value[0]
            sheet.range('C' + str(cow)).value = value[1]
            sheet.range('D' + str(cow)).value = value[2]
            sheet.range('E' + str(cow)).value = value[3]
            cow += 1


write()
workbook.save(ex_file)
app.quit
