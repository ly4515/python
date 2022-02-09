# 3_5
names = ['wang', 'zhao', 'qian', 'sun']
print(names)
name = names[1]
print(name + " can't come")
names[1] = 'li'
print(names)

# 3_6
names.insert(0, 'zhou')
print(names)
names.insert(2,'wu')
names.append('zheng')
for n in names:
    print('please eat dinner with me , ' + n)

# 3_7
sorry = names.pop()
print("sorry " + sorry)
sorry = names.pop()
print("sorry " + sorry)
sorry = names.pop()
print("sorry " + sorry)
sorry = names.pop()
print("sorry " + sorry)
sorry = names.pop()
print("sorry " + sorry)
print(names)
del names[0]
del names[0]
print(names)