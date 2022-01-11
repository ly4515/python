# 访问100次百度首页的时间，单线程
import requests
import time


def query(url):
    requests.get(url)


start = time.time()
for i in range(100):
    query('https://www.baidu.com/')
end = time.time()

print('Running time: %s Seconds' % (end-start))
