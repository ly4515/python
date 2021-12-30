path = 'D:\mine\Python\qs.txt'
with open(path) as file:
    for line in file:
        # rstrip()去除空字符
        print(line.rstrip())