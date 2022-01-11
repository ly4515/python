from bs4 import BeautifulSoup
import requests
url = 'http://exercise.kingname.info/ajax_1_postbackend'
json = {'name': 'll', 'age': 2}
respose = requests.post(url, json=json).content.decode()
print(respose)
