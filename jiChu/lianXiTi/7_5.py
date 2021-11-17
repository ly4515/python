while True:
    age = input('who old are you ')
    if 0 < int(age) < 3:
        print('free')
    elif 12 > int(age) >= 3:
        print('$10')
    elif int(age) >= 12:
        print('$15')
    else:
        print('please input you age')
        break