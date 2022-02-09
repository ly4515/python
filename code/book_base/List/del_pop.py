# del
lists = ['chun', 'xia', 'qiu', 'dong']
print(lists)     # 输出带有 []
del lists[1]
print(lists)
print("==============")

# pop    ,每用一次pop() ，都会删除一个列表元素
lists = ['chun', 'xia', 'qiu', 'dong']
print(lists)
newlist = lists.pop(2)         # 删除元素赋值给newlist
print(lists)                   # 删除元素后列表
print(newlist)                 # 被删除元素
list = lists.pop(2)
#c print(lists)
print(list)
print(lists.pop())