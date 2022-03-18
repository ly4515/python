import re

with open('D:/mine/Python/python/code/shiLi/shi.txt', 'r') as f:
    dictResult = {}

    # Find the letters each line
    for line in f.readlines():
        # remember to lower the letters
        listMatch = re.findall('[a-zA-Z]+', line.lower())

    # Count
        for eachLetter in listMatch:
            eachLetterCount = len(re.findall(eachLetter, line.lower()))
            dictResult[eachLetter] = dictResult.get(
                eachLetter, 0) + eachLetterCount

    # Sort the result
    result = sorted(dictResult.items(), key=lambda d: d[1], reverse=True)
    for each in result:
        print(each)
