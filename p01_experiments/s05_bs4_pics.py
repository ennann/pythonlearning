from bs4 import BeautifulSoup
import requests
import re



# URL needed.
url = "https://umei.cc/bizhitupian/fengjingbizhi/"
# Headers.
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
}

# First response.
response = requests.get(url, headers=headers)

# Find the web charset.
web_charset = re.compile(r'.*?charset="(.*?)">', re.S)
charset = web_charset.search(response.text).groups()[0]
print(f"***************The encoding method is: {charset}.***************")

# Decoding with specific web charset.
response.encoding = charset

# Using.
page_source = BeautifulSoup(response.text, "html.parser")

# Obtain results that contain href link. But it's my way, and I think it's better in here.
results = page_source.find_all("a", class_="TypeBigPics")

# The another way is this, and it's more logical.
# results = page_source.find("div", class_="TypeList").find_all("a", class_="TypeBigPics")

print(type(results))

for item in results:
    # print("https://umei.cc"+item.get("href"))
    sub_url = "https://umei.cc"+item.get("href")

    sub_response = requests.get(sub_url, headers=headers)
    sub_response.encoding = charset

    sub_page_source = BeautifulSoup(sub_response.text, "html.parser")

    # sub_results = sub_page_source.find_all("div", class_="ImageBody")
    #
    # I can't get the image's src in the div element, so I created a list to restore the image's src.
    # for sub_item in sub_results:
    #     print(sub_item)
    #     So far so good.
    #     print()

    # Get the sub_page image's url.
    imglists = sub_page_source.find_all("img")
    img_url = imglists[0].get("src")
    img_name = img_url.split("/")[-1]
    print(img_name, img_url)

    img_response = requests.get(img_url)
    # img_response.content


    # Add file path to the command.
    with open("/Users/Elton/Downloads/img/"+img_name, mode="wb") as f:
        f.write(img_response.content)
    print("File Saved.")

f.close()
response.close()
