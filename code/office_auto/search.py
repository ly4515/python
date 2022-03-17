'''
1.输入要查找的文件
2.支持模糊查找
3.将匹配的文件信息存放到一个列表中
4.打印所有符合的文件信息
'''

from pathlib import Path

while True:
    folder = input('请输入要查找的路径:')
    folder = Path(folder.strip())
    if folder.exists() and folder.is_dir():
        break
    else:
        print('路径有误，重新输入')

search = input('输入要查找的文件或文件夹')
result = folder.rglob(f'*{search}*')

if not result:
    print(f'在{folder}下未找到{search}相关内容')
else:
    result_folder = []
    result_file = []
    for i in result:
        if i.is_dir():
            result_folder.append(i)
        else:
            result_file.append(i)
    if result_folder:
        print(f'包含{search}的文件夹有:')
        for i in result_folder:
            print(i)
    if result_file:
        print(f'包含{search}的文件有:')
        for i in result_file:
            print(i)
