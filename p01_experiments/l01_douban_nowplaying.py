import requests
from lxml import etree
import re
import csv
import time


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
}


url = 'https://movie.douban.com/cinema/nowplaying/hangzhou/'

response = requests.get(url, headers=headers)
source_code = response.text
# Get tree structure.
tree = etree.HTML(source_code)

"""
//*[@id="nowplaying"]/div[2]/ul
/html/body/div[3]/div[1]/div/div[1]/div[3]/div[2]/ul
/html/body/div[3]/div[1]/div/div[1]/div[3]/div[2]/ul/li[1]
"""

lists = tree.xpath('/html/body/div[3]/div[1]/div/div[1]/div[3]/div[2]/ul/li')
print(type(lists))
print(len(lists))

print(lists)


time.sleep(2)

response.close()
