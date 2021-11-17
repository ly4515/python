# sorted() 方法获得特定顺序排列的建列表
languages = {
    'jen': 'python',
    'sarsh': 'C',
    'edward': 'ruby',
    'phil': 'python'
    }
for name in sorted(languages.keys()):
    print(name.title() + ', think you for taking the poll')
print('======================')

# 遍历字典的值
for lan in languages.values():
    print(lan)
print('======================')

# 集合set 每个元素都是唯一的，可剔除重复项
for lan in set(languages.values()):
    print(lan)