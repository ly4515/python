# 任一个英文的纯文本文件，统计其中的单词出现的个数

file = 'D:/mine/Python/python/code/shiLi/shi.txt'
word_count = {}
with open(file, 'r') as f:
    word_list = f.read().lower().replace('\n', ' ').split()
    # word_list = word_list.split()
    for word in word_list:
        if word not in word_count.keys():
            count = 1
            word_count[word] = count
        else:
            count = word_count.get(word)
            count += 1
            word_count[word] = count

for k, v in word_count.items():
    print(f'{k}出现了{v}次')
