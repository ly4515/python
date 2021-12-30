import json
with open('number.json') as file:
    num = json.load(file)

print(num)