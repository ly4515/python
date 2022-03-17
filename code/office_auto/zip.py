'''
1.找出指定目录下距离上次修改时间超过一个月的md文件
2.将所有文件重命名，在原本文件名开头加上最后修改日期
3.创建新文件夹：长期未使用
4.将所有文件移动到 长期未使用 文件夹
5.对 长期未使用 文件夹进行压缩处理，并在名字上加上今天日期
'''

from datetime import datetime
import os
import shutil
import zipfile

path = input('请输入路径:')
os.chdir(path)

file_list = []
for dirpath, dirnames, files in os.walk('./'):
    for file in os.scandir(dirpath):
        if not file.is_dir():
            # 文件时间戳
            file_time = file.stat().st_mtime
            # fromtimestamp格式化时间戳
            file_datetime = datetime.fromtimestamp(file_time)
            # 时间差
            datetime_delta = datetime.now()-file_datetime
            if datetime_delta.days >= 1 and file.name.endswith('.md'):
                new_name = f"{file_datetime.strftime('%Y-%m-%d')}-{file.name}"
                # 重命名
                os.rename(dirpath+'/'+file.name, new_name)
                file_list.append(new_name)

if not os.path.exists('长期未使用'):
    os.mkdir('长期未使用')

for file1 in file_list:
    shutil.move(file1, '长期未使用/')

os.chdir('长期未使用/')
zipfile_list = os.listdir('./')

zip_filename = f'{datetime.now().strftime("%Y-%m-%d")}_长期未使用.zip'
with zipfile.ZipFile(zip_filename, 'w') as zipobj:
    for file in zipfile_list:
        zipobj.write(file)
