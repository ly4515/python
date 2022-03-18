# 生成 200 个激活码,激活码是唯一的二十位数字和拉丁字母的序列,格式为 xxxxx-xxxxx-xxxxx-xxxxx

import random
import string


def sc_jhm():
    i = 0
    five_zifu = ''
    jhm_list = []
    zifu = string.digits+string.ascii_letters
    while i < 4:
        for j in range(5):
            one_zifu = random.choice(zifu)
            five_zifu += one_zifu
        i += 1
        five_zifu = five_zifu+'-'
        jhm = five_zifu.strip('-')
    if jhm not in jhm_list:
        jhm_list.append(jhm)
    for j in jhm_list:
        print(j)


def jhm_num(num):
    for i in range(num):
        sc_jhm()


num = int(input('激活码数量:'))
jhm_num(num)
