cities = {
    'changchun': {'country': 'china', 'population': '7877788', 'fact': 'cold'},
    'new': {'country': 'amication', 'population': '1256500', 'fact': 'hot'},
    'france': {'country': 'fance', 'population': '456110', 'fact': 'win'},
    }

for key, value in cities.items():
    print('key: ' + key.title())
    print('value: ' + str(value))
print('==========================')

for k, v in cities.items():
    print(k, ":")
    for key, value in v.items():
        print("\t", key, ":", value)

