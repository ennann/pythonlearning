import csv
import time
import requests
from lxml import etree

url = "https://beijing.zbj.com/search/f/?kw=saas"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
}


# Get response.
response = requests.get(url=url, headers=headers)

# Check HTTP conntection. If doesn't work, break.
status_code = response.status_code
if status_code != 200:
    print("You need to check the network connection.")
    breakpoint()

# Decode the PageSource.
page = response.text

# Get tree file.
tree = etree.HTML(page)


'''
For comparison.
/html/body/div[6]/div/div/div[2]/div[5]/div[1]
/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div[1]
/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div[1]
第一个价格
/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div[1]/div/div/a[2]/div[2]/div[1]/span[1]
/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div[2]/div/div/a[2]/div[2]/div[1]/span[1]
/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div[1]/div/div/a[1]/div[1]/p/text()




'''

lists = tree.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div')
print(len(lists))
print(tree.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div[1]/div/div/a[2]/div[2]/div[1]/span[1]/text()'))


for item in lists:
    shop_name = tree.xpath('.//div/div/a[1]/div[1]/p/text()')
    print(shop_name)

    item_name = tree.xpath('.//div[1]/div[1]/div/div/a[2]/div[2]/div[2]/p/text()')
    print(item_name)

    item_price = tree.xpath(".//div/div/a[2]/div[2]/div[1]/span[1]/text()")
    print(item_price)
    break


    print()
