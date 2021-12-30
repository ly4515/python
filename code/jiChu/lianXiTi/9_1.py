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


restaurant = Restaurant('j', 'o')
print(restaurant.resaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()