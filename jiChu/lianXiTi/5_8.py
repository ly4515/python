names = ['admin', 'mary', 'jone', 'eric', 'infd']
# names = []

# if 判断列表是否为空，不为空返回True，为空返回False
if names:
    for name in names:
        if name == 'admin':
            print("Hello admin")
        else:
            print("Hello " + name.title() + " .")
else:
    print("we need some users")