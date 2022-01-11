import requests
import json
import re

url = 'http://exercise.kingname.info/exercise_ajax_3.html'
first_url = 'http://exercise.kingname.info/ajax_3_backend'
second_url = 'http://exercise.kingname.info/ajax_3_postbackend'

page_html = requests.get(url).content.decode()
secret_2 = re.search("secret_2 = '(.*?)'", page_html, re.S).group(1)

ajax_json = requests.get(first_url).content.decode()
ajax_dict = json.loads(ajax_json)
secret_1 = ajax_dict['code']

ajax_2_json = requests.post(second_url, json={'name': 'kk',
                                              'age': 24,
                                              'secret1': secret_1,
                                              'secret2': secret_2}).content.decode()
ajax_2_dict = json.loads(ajax_2_json)
code = ajax_2_dict['code']
print(code)
