# 访问100次百度首页的时间，多线程
from multiprocessing.dummy import Pool
import requests
import time


def query(url):
    requests.get(url)


start = time.time()
url_list = []
for i in range(100):
    url_list.append('https://www.baidu.com/')

pool = Pool(5)
pool.map(query, url_list)

end = time.time()
print('Running time: %s Seconds' % (end-start))
