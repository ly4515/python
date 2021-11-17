class Restaurant():
    # 属性
    def __init__(self, resaurant_name, cuisine_type):
        self.resaurant_name = resaurant_name
        self.cuisine_type = cuisine_type


    # 方法
    def describe_restaurant(self):
        print(self.resaurant_name + ' type is ' + self.cuisine_type)


    def open_restaurant(self):
        print('now is open')

'''
restaurant = Restaurant('j', 'o')
print(restaurant.resaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
'''

class IceCreamStand(Restaurant):
    def __init__(self, resaurant_name, cuisine_type):
        '''初始化父类属性
        super()._init_() -> 正确
        super._init_() -> 错误
        '''
        super().__init__(resaurant_name, cuisine_type)
        '''初始化子类特有属性'''
        self.flavors = []

    '''子类特有方法'''
    def ice(self):
        print('make a ice')


iceCreamStand = IceCreamStand('kk', 'M')
iceCreamStand.ice()
