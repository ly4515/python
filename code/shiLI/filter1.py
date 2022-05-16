# 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，
# 则变成「**是个好城市」

words = []
with open('D:/mine/Python/python/code/shiLi/filtered_words.txt', 'r', encoding='utf-8') as f:
    for line in f:
        words.append(line.strip())
        while True:
            text = input('输入词语：').strip()
            for word in words:
                if word in text:
                    new_w = '*'*len(word)
                    text = text.replace(word, new_w)
            print(text)
