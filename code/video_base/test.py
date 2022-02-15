'''
掷色子游戏，2个骰子
1.玩游戏要有金币，没有金币不能玩游戏
2.玩游戏赠金币一枚，充值获取金币
3.充值要是10的倍数，每10元充值20枚金币
4.每次游戏消耗5枚金币
5.游戏输赢: 猜大小，猜对奖励7枚金币，猜错没有奖励，超出6点以上为大，否则是小
6.结束游戏: 1）主动退出  2）没有金币退出
7.只要退出则打印剩余金币数，共玩了几局
'''

import random


coins = 0
count = 0
while True:
    if coins < 5:
        print("金币不足，请充值")
        while True:
            money = int(input("请输入充值数"))
            if money % 10 == 0:
                coins += money/10*20
                print("充值成功，当前金币为: ", coins)
                choice = input('是否开始游戏，y/n?')
                if coins >= 5 and choice == 'y':
                    coins -= 5
                    ran1 = random.randint(1, 6)
                    ran2 = random.randint(1, 6)
                    guss = input("请猜大小")
                    if ran1+ran2 > 6 and guss == '大' or ran1+ran2 <= 6 and guss == '小':
                        print("恭喜，你赢了")
                        coins += 1
                        coins += 7
                        print("剩余金币{}".format(coins))
                        y_or_n = input("是否继续 y/n?")
                        if y_or_n == "n":
                            break
                        else:
                            if coins < 5:
                                break
                    else:
                        print("很遗憾，你输了")
                        coins += 1
                        print("剩余金币{}".format(coins))
                        y_or_n = input("是否继续 y/n?")
                        if y_or_n == "n":
                            break
                        else:
                            if coins < 5:
                                break
                    count += 1
                else:
                    break
            else:
                print("需要充值10的倍数")

print("金币数{}，共玩{}局。".format(coins, count))
