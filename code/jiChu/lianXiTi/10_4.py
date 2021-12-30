while True:
    with open('user.txt', 'a')as file:
        name = input("what's you name")
        hi = 'hello ' + name.title()
        if name == 'q':
            break
        print(hi)
        file.write(name + '\n')
        file.write(hi + '\n')
