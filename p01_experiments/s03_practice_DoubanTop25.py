# Obtain Douban Top 25 List, Storage as json File.
import re

import requests

# URL of Douban top lists.
url = "https://movie.douban.com/top250"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
}

# Check the http status.
response = requests.get(url=url, headers=headers)

print(f"The HTTP status code is: {response.status_code}")

# GET page source code.
page_contents = response.text

# print(page_contents)
# Regular expression to obtain name
# preload re
## When I was trying to get the year, I use \d+ to obtain. Turned out that is really slow.

obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<span class="playable">(?P<playable>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                 r'<span class="rating_num" property="v:average">(?P<rating>.*?)'
                 r'</span>.*?<span>(?P<number>.*?)</span>', re.S)

results = obj.finditer(page_contents)
print(results.group())

# Close connection.
response.close()
