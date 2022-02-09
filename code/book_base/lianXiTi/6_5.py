rolls = {'dwd': 'china', 'fji': 'jiol', 'nile': 'egypt'}
# items()获取字典的键值
for r, n in rolls.items():
    print("The " + r.title() + "run through " + n.title())

for r in set(rolls.keys()):
    print(r.title())

for n in set(rolls.values()):
    print(n.title())