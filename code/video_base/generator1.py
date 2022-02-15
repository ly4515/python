# 只要函数中出现了yield关键字，函数就变成生成器了


def func():
    n = 0
    while True:
        n += 1
        yield n


a = func()
print(next(a))
print(next(a))
print(next(a))
print(a.__next__())
