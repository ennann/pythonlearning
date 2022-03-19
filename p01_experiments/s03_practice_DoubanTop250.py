# Obtain Douban Top 25 List, Storage as csv File.
import requests
import re
import csv
import time


# URL of Douban top lists.
url = "https://movie.douban.com/top250"

# Defining headers.
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
}


# Pre-load R.E.
# add ranking to double check any info was lost.
obj = re.compile(r'<li>.*?<em class="">(?P<ranking>.*?)'
                 r'</em>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<span class="playable">(?P<playable>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                 r'<span class="rating_num" property="v:average">(?P<rating>.*?)'
                 r'</span>.*?<span>(?P<number>.*?)</span>', re.S)


# The first param.
start = 0

# Using for lop to GET Douban Top 250, by increase 25 each time.
for i in range(0, 10):
    param = {
        "start": start,
            "filter": ""
    }

    response = requests.get(url=url, headers=headers, params=param)


    # Check HTTP conntection is OK or not.
    status_code = response.status_code
    if status_code != 200:
        print("You need to check the network connection, may be your IP was blocked by Douban.")
        break

    # Finding the charset code.
    web_charset = re.compile(r'.*?charset=(.*?)">', re.S)
    charset = web_charset.search(response.text).groups()[0]
    # Show the web_charset.
    print(f"***************The encoding method is: {charset}.***************")


    # Trans to text.
    source_code = response.text

    # Using R.E. to find key info.
    results = obj.finditer(source_code)

    # Creating a csv file.
    f = open("top250.csv", mode="w")
    csvwriter = csv.writer(f)

    for it in results:
        # In my first thought, I want to creat a list/dict, but it didn't work.
        # line = {
        # it.group("name"), it.group("year").strip(), it.group("rating"), it.group("number"), it.group("playable")
        # }

        # More elegant way to do it.
        dic = it.groupdict()
        dic["year"] = dic["year"].strip()
        csvwriter.writerow(dic.values())

    # To remind.
    print(f"Getting Top 250 lists from {start+1} to {start+25}")

    # Increasing param by 25
    start += 25

    # Make code more like human.
    time.sleep(6)

    # Close file.
    f.close()

# Close connection.
response.close()
