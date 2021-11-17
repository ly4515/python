message = 'please tell me something'
message += "\nif you input 'quit' will stop"
m = ''  # 变量初始化，否则会报错  NameError: name 'm' is not defined
while m != 'quit':
    m = input(message)
    if m != 'quit':
        print(m)
