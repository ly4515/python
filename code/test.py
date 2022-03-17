'''
1.找出指定目录下距离上次修改时间超过一个月的md文件
2.将所有文件重命名，在原本文件名开头加上最后修改日期
3.创建新文件夹：长期未使用
4.将所有文件移动到 长期未使用 文件夹
5.对 长期未使用 文件夹进行压缩处理，并在名字上加上今天日期
'''

import os
import datetime
import shutil
import zipfile

path = input('请输入路径:')
os.chdir(path)

file_list = []
for dirpath, dirnames, fiels in os.walk('./'):
    # 返回迭代器
    for file in os.scandir(dirpath):
        if file.is_file:
            file_mtime = datetime.datetime.fromtimestamp(file.stat().st_mtime)
            date_c = datetime.datetime.now()-file_mtime
            if date_c.days >= 1 and file.name.endswith('.md'):
                new_name = f"{file_mtime.strftime('%Y-%m-%d')}-{file.name}"
                os.rename(file.name, new_name)
                file_list.append(new_name)

if not os.path.exists('长期未使用'):
    os.mkdir('长期未使用')

for file1 in file_list:
    shutil.move(file1, '长期未使用/')

os.chdir('长期未使用/')
zipfile_list = os.listdir('./')

zip_filename = f'{datetime.datetime.now().strftime("%Y-%m-%d")}_长期未使用.zip'
with zipfile.ZipFile(zip_filename, 'w') as zipobj:
    for file in zipfile_list:
        zipobj.write(file)
