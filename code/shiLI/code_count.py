# 有个文件，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

from calendar import c
import re

temp = zhu_shi = code = 0
file = 'D:/mine/Python/python/code/shiLi/ji_huo_ma.py'

with open(file, 'r', encoding='utf-8') as f:
    result = f.read()
    temp_count = re.findall('^$', result)
    print(temp_count)
    zhu_shi_count = re.findall('^#.*', result)
    print(zhu_shi_count)
    if result == temp:
        temp += 1
    elif result == zhu_shi:
        zhu_shi += 1
    else:
        code += 1
num = temp+zhu_shi+code
print(f'空行:{temp},注释:{zhu_shi},代码:{code},共:{num}')
