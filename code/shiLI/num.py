import re
str_test = input("请输入：")

# 把正则表达式编译成对象,如果经常使用该对象,此种方式可提高一定效率
num_regex = re.compile(r'[0-9]')
zimu_regex = re.compile(r'[a-zA-z]')
hanzi_regex = re.compile(r'[\u4E00-\u9FA5]')

print('输入字符串:', str_test)
# findall获取字符串中所有匹配的字符
num_list = num_regex.findall(str_test)
print('包含的数字:', num_list)
zimu_list = zimu_regex.findall(str_test)
print('包含的字母:', zimu_list)
hanzi_list = hanzi_regex.findall(str_test)
print('包含的汉字:', hanzi_list)
