print('give me two num, i will divide them')
print("enter 'q' to exit")
while True:
    num1 = input('first num:')
    if num1 == 'q':
        break
    num2 = input('second num:')
    if num2 == 'q':
        break
    try:
        num = int(num1)/int(num2)
    except ZeroDivisionError:
        print("不能除0")
    else:
        print('sum: ' + str(num))