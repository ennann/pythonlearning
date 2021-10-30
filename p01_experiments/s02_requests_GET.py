import requests
from pprint import pprint

# Douban
url = "https://movie.douban.com/j/chart/top_list"

# Fix headers for Douban.
headers = {
    "Cookie": "",

    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
}

# Load the param of Douban top love movie list into the utl.
param = {
        "type": "13",
        "interval_id": "100:90",
        "action": "",
        "start": start,
        "limit": 20
    }


# Using for loop to obtain Douban love movie list Top 100.
for start in range(0,5):

    param = {
        "type": "13",
        "interval_id": "100:90",
        "action": "",
        "start": start,
        "limit": 20
    }

    # Return results.
    response = requests.get(url=url, headers=headers, params=param)


    print(f"The HTTP status code is: [{response.status_code}].")
    print(response.request.url)
    # print(response.request.headers)
    print()
    # pprint(response.json())
    start = start + 20
    with open("Douban_love_movie.txt", mode="w") as f:
        f.write(response.text)