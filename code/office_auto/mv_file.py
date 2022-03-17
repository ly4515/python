'''
1.键盘输入一个路径
2.获取里面所有mp4文件
3.重命名mp4文件，在每个文件前加前缀，前缀为文件最后修改的年月日（2021-08-18_西游记01.mp4）
4.新建文件夹：最新视频
5.将重命名的视频批量移动到最新视频文件夹
'''

import os
import shutil
import datetime
import glob

path = input("请输入路径:")
os.chdir(path)

# os.walk 遍历，返回文件夹所在路径，文件夹下所有目录名字，文件夹下所有文件
for dirpath, dirnames, files in os.walk('./'):
    # os.scandir 返回迭代器
    for file in os.scandir(dirpath):
        if file.name.endswith('.mp4'):
            tm = datetime.datetime.fromtimestamp(file.stat().st_mtime)
            new_file = str(tm.year)+'-'+str(tm.month) + \
                '-'+str(tm.day)+'-'+file.name
            os.rename(dirpath+'/'+file.name, new_file)

if not os.path.exists('最新视频'):
    os.mkdir('最新视频')

# glob.glob 将某目录下所有跟通配符模式相同的文件放到一个列表中
file_list = glob.glob('*.mp4')
for name in file_list:
    shutil.move(name, '最新视频/')
print('移动完成！')
