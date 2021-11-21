from bs4 import BeautifulSoup
import requests
import re


url = "https://movie.douban.com/top250"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
}

responce = requests.get(url, headers=headers)

obj = re.compile(r'.*?<a href="(?P<link>.*?)" class="">.*?', re.S)

# BeautifulSupe

page = BeautifulSoup(responce.text, "html.parser")
# find & find_all
# find: only find the first one, find-all: find all

results = page.find_all("div", class_="info")
lists = page.find_all("div", attrs={"class": "info"})

for item in lists:
    name = item.find_all("span", attrs={"class": "title"})
    link = re.search()
    print(name[0].text)