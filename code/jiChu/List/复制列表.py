# 切片复制
players = ['charles', 'martina', 'michael', 'florece', 'eli']
new_players = players[:]
print(players)
print(new_players)
players.append('Jone')
new_players.append('Marry')
print(players)
print(new_players)

print("=============")

# for循环复制列表，麻烦
players = ['charles', 'martina', 'michael', 'florece', 'eli']
new_players = []
for player in players:
    new_players.append(player)
print(players)
print(new_players)
players.append('Jone')
new_players.append('Marry')
print(players)
print(new_players)
