#

from bs4 import BeautifulSoup
import requests
import json



headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
r = requests.get('https://www.baidu.com/')

print(r.status_code)
# print(r.text)
print(r.json())
soup = BeautifulSoup(html, 'lxml')
