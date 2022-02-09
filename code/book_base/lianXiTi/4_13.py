foods = ('a', 'b', 'c', 'd', 'e')
for food in foods:
    print(food)
# 不能修改元组元素
# foods[0] = 'f'

print('===========')

# 可修改元组变量
foods = ('a', 'g', 'c', 'r', 'e')
for food in foods:
    print(food)