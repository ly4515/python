players = ['charles', 'martina', 'michael', 'florece', 'eli']
print(players[0:3])      # 包头不包尾
print(players[:4])       # 未指定第一个索引，从0索引开始
print(players[3:])       # 未指定最后一个索引，到列表结尾
print(players[-3:])      # 用负数索引


# 遍历切片
for player in players[:3]:
    print(player.title())