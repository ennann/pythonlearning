import requests
from lxml import etree
import re
import csv
import time


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
}


url = "https://movie.douban.com/j/search_subjects?type=movie&tag=热门&sort=recommend&watched=on&page_limit=20&page_start=0"
# url = "http://httpbin.org/get"

response = requests.get(url, headers=headers, cookies=cookies)
print(response.json())




'''
Totally wrong. This url returns a json file, but I still decode it by using HTML. 
And when I running the Xpath, of course the XPath return null. 
'''

#
# source_code = response.text
# tree = etree.HTML(source_code)
#
#
# # results = tree.xpath("//*[@id='content']/div/div[1]/div/div[4]/div")
# """
# XPath compare:
# //*[@id="content"]/div/div[1]/div/div[4]/div
# //*[@id="content"]/div/div[1]/div/div[4]/div/a[1]               第一个列表
# //*[@id="content"]/div/div[1]/div/div[4]/div/a[1]/p/text()      电影名字
# //*[@id="content"]/div/div[1]/div/div[4]/div/a[1]/div/img       电影封面
# //*[@id="content"]/div/div[1]/div/div[4]/div/a[2]               第二个
#
# /html/body/div[3]/div[1]/div/div[1]/div/div[4]/div
# /html/body/div[3]/div[1]/div/div[1]/div/div[4]/div/a[1]         第一个元素
# /html/body/div[3]/div[1]/div/div[1]/div/div[4]/div/a[1]/p       电影名字
# /html/body/div[3]/div[1]/div/div[1]/div/div[4]/div/a[1]/div/img 电影封面
# /html/body/div[3]/div[1]/div/div[1]/div/div[4]/div/a[1]/p/strong 评分
# /html/body/div[3]/div[1]/div/div[1]/div/div[4]/div/a[2]         第二个
#
#
#
# """
#
#
#
# lists = tree.xpath('//div/div[4]/div/a')
# print(type(lists))
# print(len(lists))
#
# print(lists)
#

time.sleep(0.1)

response.close()
