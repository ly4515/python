# 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
def filter():
    words = []
    with open('D:/mine/Python/python/code/shiLi/filtered_words.txt', 'r', encoding='utf-8') as f:
        for line in f:
            words.append(line.strip())
    return words


def input_word():
    while True:
        words = filter()
        word = input('输入词语,q退出:').strip()
        if word in words:
            print('Freedom')
        elif word == 'q':
            break
        else:
            print('Human Rights')


input_word()
