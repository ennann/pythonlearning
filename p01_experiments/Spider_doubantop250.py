# Download Douban Top 250 Lists as json File.


from urllib.request import urlopen
import requests

url = "https://movie.douban.com/top250"
headers = {
    "Cookie": "cookies content",
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
}

# Check teh status code of http protocol.
response = requests.get(url, headers = headers)
print(f"The HTTP response is : {response.status_code}")


results = urlopen(url)
print(results.read().decode('utf-8'))
print(results.content)