import requests

session = requests.session()

"""
session  是一个连续的对话，这样可以做到保存 cookie。
但是在浏览器中是可以直接保存的，因此在程序中使用这样的方式去保存 cookies

1. 第一步是


"""

url = 'https://movie.douban.com/mine'

# Defining browser headers.
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
    'Cookies': 'bid=5RTa-QUyfmY; ap_v=0,6.0; dbcl2="123168639:2MWL7MQq0nU"'
}

response = requests.get(url, headers=headers)

page = response.text
print(page)