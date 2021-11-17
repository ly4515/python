def car_info(manufacturer, size, **info):
    cars = {}
    cars['manufacturer_info'] = manufacturer
    cars['size_info'] = size
    for k, v in info.items():
        cars[k] = v
    return cars


car = car_info('yadi', 'M', color='bule', tow_package=True)
print(car)