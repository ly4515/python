with open('a.txt', 'a') as f:
    f.writelines('hello\n')
    f.write('hi\n')

with open('a.txt', 'r') as f:
    line = f.readline()
    print(line)
