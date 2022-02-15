'''
掷色子游戏,2个骰子
1.玩游戏要有金币,没有金币不能玩游戏
2.玩游戏赠金币一枚,充值获取金币
3.充值要是10的倍数,每10元充值20枚金币
4.每次游戏消耗5枚金币
5.游戏输赢: 猜大小,猜对奖励7枚金币,猜错没有奖励,超出6点以上为大,否则是小
6.结束游戏: 1)主动退出  2)没有金币退出
7.只要退出则打印剩余金币数,共玩了几局
'''

import random


coins = 0
count = 0
while True:
    if coins >= 5:
        choice = input("是否开始游戏,y/n?")
        if choice == 'y':
            count += 1
            coins -= 5
            int1 = random.randint(1, 6)
            int2 = random.randint(1, 6)
            guess = input("请猜大小: ")
            if guess == "大" and int1+int2 > 6 or guess == "小" and int1+int2 <= 6:
                coins += 7
                coins += 1
                print("恭喜,你赢了!当前金币为{}".format(coins))
                go = input("是否继续游戏,y/n?")
                if go == 'n':
                    break
            else:
                coins += 1
                print("很遗憾,你输了。当前金币为{}".format(coins))
                if coins < 5:
                    print("金币不足,游戏退出")
                    break
                go = input("是否继续游戏,y/n?")
                if go == 'n':
                    break
        else:
            break
    else:
        print("金币不足,请充值")
        money = int(input("请输入充值金额"))
        if money % 5 == 0:
            coins += money/10*20
            print("充值成功,当前金币为{}".format(coins))
        else:
            print("只能充值10的倍数")
print("当前金币数{},共玩了{}局。".format(coins, count))
