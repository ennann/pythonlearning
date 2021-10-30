import requests
from pprint import pprint


print("Powered by Baidu Translation.")

word = input("Please input the word you want to find: ")
url = "https://fanyi.baidu.com/sug"
headers = {
    "Cookie": "IPLOC=CN1100; SUID=635948DF1431A40A00000000617CB1F1; SUV=1635561970123295; browerV=3; osV=2; ABTEST=0|1635561975|v17; SNUID=D3F6F86FAFAA60275D1A1AD8B054B072; sst0=905; ld=cZllllllll2PKa4illlllpVD7kDlllllT1PBYZllllGlllll4klll5@@@@@@@@@@",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
}
data = {
    "kw": word
}

response = requests.post(url, headers=headers, data=data)
pprint(response.json())