class Restaurant():
    # 属性
    def __init__(self, resaurant_name, cuisine_type):
        self.resaurant_name = resaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    # 方法
    def describe_restaurant(self):
        print(self.resaurant_name + ' type is ' + self.cuisine_type)

    def open_restaurant(self):
        print('now is open')

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served = number + 3

restaurant = Restaurant('j', 'o')
print(restaurant.resaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

print('num:' + str(restaurant.number_served))
restaurant.number_served = 5
print('new_num:' + str(restaurant.number_served))
restaurant.set_number_served(9)
print('set_new_num:' + str(restaurant.number_served))
restaurant.increment_number_served(8)
print('add_new_num:' + str(restaurant.number_served))


