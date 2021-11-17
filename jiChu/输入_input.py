message = "please input your name"
# 可用 += 拼接输入的提示信息
message += "your first name is: "
name = input(message)

age = input('how old are you ')
int(age) < 18       # input 获取的是字符串，若想要数字类型需要转换
print('hello, ' + name)
print('you are a kid')