import requests

"""
1. M3U8 file
2. Download ts file through M3U8
3. join ts file to MP4 file

Case
1. get page source
2. get M3U8 link
3. download M3U8 file 
4. read M3U8 file,download video
5. join video
"""

url = "https://91kanju.com/vod-play/62235-2-1.html"
# url = "https://www.baidu.com/"

proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
}

# conn = TCPConnector(ssl=False)
response = requests.get(url, headers=headers, proxies=proxies)

status_code = response.status_code
if status_code != 200:
    print("You need to check the network connection, may be your IP was blocked.")

print(response.text)
