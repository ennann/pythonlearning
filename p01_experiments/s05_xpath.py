from lxml import etree
import requests

url = "https://movie.douban.com/top250"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
}

response = requests.get(url, headers=headers)

page = response.text
tree = etree.HTML(page)


# 使用 xpath 来解析 HTML 文件，并且获取豆瓣电影的多种姓名。
# results = tree.xpath('/html//ol//span[@class="title"]/text()')

results = tree.xpath('/html//ol//span[@class="title"]')
print(results)

# for item in results:
    # 拿到属性的值
    # print(item.xpath('./@class'))
    # print(item.xpath('./text()'))



# 快速查看页面中的 Xpath
# /html/body/div[3]/div[1]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]

# 豆瓣 list
#
# /html/body/div[3]/div[1]/div/div[1]/ol/li[1]
# /html/body/div[3]/div[1]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]

print(tree.xpath('/html/body/div[3]/div[1]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]/text()'))
