'''引入json'''
import json
num = [1, 3, 5, 7, 9]
'''通常使用扩展名 .json来指出文件存储的数据为JSON格式'''
with open('number.json', 'w') as file:
    json.dump(num, file)