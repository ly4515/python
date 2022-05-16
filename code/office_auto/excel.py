import xlwings
import os

# visible Ture:可见excel,False：不可见excel,
# add_book True: 打开excel并且新建工作簿,False：不新建工作簿
# 应用程序
app = xlwings.App(visible=True, add_book=False)
if not os.path.exists('./a.xls'):
    # 新建excel工作簿
    excel = app.books.add()
    excel.save('a.xls')
    print('a.xls已创建')
wb = app.books.open('./a.xls')
# wb.sheets['sheet3'].delete()
# 添加sheet页
# wb.sheets.add("sheet4")
# 当前活跃工作簿
# print(wb.app.activate)
# 当前活跃工作表
# print(wb.sheets.active)
sheet = wb.sheets('sheet1')
sheet.range('A1').value = 'A1'
sheet.range('A2').value = [1, 2, 33]
sheet.range("A4:B5").value = [[1, 2], [3, 4]]
wb.save('./a.xls')
app.quit()
