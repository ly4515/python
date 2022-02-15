g = (x*3 for x in range(10))
while True:
    try:
        e = next(g)
        print(e)
    except:
        print('没有更多元素了')
        break
