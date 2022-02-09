# 一个星号创建空元祖，传递任意数量的实参
def make(*toppings):
    for top in toppings:
        print('add ' + top)


make('a')
make('a', 'b')
make('a', 'b', 'c')