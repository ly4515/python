import json
filename = 'userinfo.json'
try:
    with open(filename) as file:
        name = json.load(file)
except FileNotFoundError:
    name = input('what is your name ')
    with open(filename, 'w') as file:
        json.dump(name, file)
        #pass
else:
    print('hello, ' + name.title())