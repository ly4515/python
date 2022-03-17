import os
import zipfile

os.chdir('D:/mine/Python/python/code/office_auto')
dir_list = os.listdir()
with zipfile.ZipFile('mypyfile.zip', 'w') as zipobj:
    for file in dir_list:
        if file.endswith('.py'):
            zipobj.write(file)

with zipfile.ZipFile('mypyfile.zip', 'r') as zipobj:
    # 查看压缩文件
    print(zipobj.namelist())

with zipfile.ZipFile('mypyfile.zip', 'r') as zipobj:
    # 解压一个文件
    # zipobj.extract('rw_file.py', 'file')
    # 解压所有文件
    zipobj.extractall('file/')
