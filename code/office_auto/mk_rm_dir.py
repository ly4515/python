import os

if os.path.exists('D:/mine/Python/python/test'):
    print(os.getcwd)
else:
    os.makedirs('D:/mine/Python/python/test/01')
    print("目录已创建")

os.removedirs('D:/mine/Python/python/test/01')
