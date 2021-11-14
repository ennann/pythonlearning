import requests
import re
import csv
import time


# Simulate Chrome Action.
domain = "https://www.dytt89.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
                  " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
}

response = requests.get(domain, headers=headers, verify=False)

# Check HTTP response code.
print(f"***************The HTTP response code is: {response.status_code}.***************")

# Finding the charset code.
web_charset = re.compile(r'.*?charset=(.*?)">', re.S)
charset = web_charset.search(response.text).groups()[0]
print(f"***************The encoding method is: {charset}.***************")

# Change to the SourceCode encoding type.
response.encoding = charset

obj1 = re.compile(r"2021必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'.*?◎片　　名　(?P<movie_name>.*?)<br />.*?#fdfddf"><a href="(?P<download_link>.*?)">.*?', re.S)

results1 = obj1.finditer(response.text)
# print(results1)
suburl_list = []
for it in results1:
    ul = it.group("ul")

    results2 = obj2.finditer(ul)
    for itt in results2:
        suburl = domain + itt.group("href").strip("/")
        suburl_list.append(suburl)


for href in suburl_list:
    sub_web = requests.get(href, headers=headers)
    sub_web.encoding = charset
    results3 = obj3.search(sub_web.text)
    # print(results3.groups("movie_name"))
    # print( results3.groups("download_link"))
    f = open("top250.csv", mode="w")
    csvwriter = csv.writer(f)
    csvwriter.writerow(dic.values())

f.close()
response.close()