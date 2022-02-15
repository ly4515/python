list = [1, 2, 3, 4]
# [表达式 for 变量 in 列表]

list1 = [x+2 for x in list]

# [表达式 for 变量 in 列表 if 条件]
list2 = [x+2 for x in list if x % 2 == 0]

# [表达式A if 条件 else 表达式B for 变量 in 列表]
list3 = [x+2 if x % 2 == 0 else x+1 for x in list]
print(list1)
print(list2)
print(list3)
