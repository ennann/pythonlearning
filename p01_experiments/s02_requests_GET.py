import requests
from pprint import pprint

# Douban
url = "https://movie.douban.com/j/chart/top_list"

# Fix headers for Douban.
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
}

# Load the param of Douban top love movie list into the utl.
love_param = {
        "type": "13",
        "interval_id": "100:90",
        "action": "",
        "start": 0,
        "limit": 20
    }


# Using for loop to obtain Douban love movie list Top 100.
# love movies 13, sci-fic movie 17.
start = 0
for start in range(0,5):

    param = {
        "type": "17",
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
    with open("Douban_love_movie.txt", mode="w") as f:
        f.write(response.text)
    start = (start + 1) * 20

# Otherwise, 403
response.close()