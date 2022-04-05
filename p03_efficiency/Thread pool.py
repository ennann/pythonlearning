from concurrent.futures import ThreadPoolExecutor
import requests
import time
from lxml import etree
import csv

# basic_url = "https://www.guo68.com/market?page=1"

def get_fruit_price(url):

    # Set Headers.
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
    }

    # Get response.
    response = requests.get(url, headers=headers)

    # Check HTTP connection. If it doesn't work, break.
    status_code = response.status_code
    if status_code != 200:
        print("You need to check the network connection, may be your IP was blocked.")
        # break

    # Decode the PageSource.
    page = response.text

    # Get tree file.
    tree = etree.HTML(page)

    table = tree.xpath("/html/body/div[3]/div/div[1]/div[3]/div[2]")[0]
    #                  "/html/body/div[3]/div/div[1]/div[3]/div[2]/ul[2]/a/li[1]"

    # Get all the contents in table. But leave the table header.
    # uls = table.xpath("./ul")[1:]
    uls = table.xpath("./ul[position()>1]")

    # Create a CSV File.
    f = open("/Users/Elton/Downloads/FruitPrice.csv", mode="a")
    csvwriter = csv.writer(f)

    for ul in uls:
        content = ul.xpath("./a/li/text()")
        # Data Process
        content = (item.replace("/", "每") for item in content)
        # print(list(content))

        # Write data to csv file.
        csvwriter.writerow(content)

    print(url, "Download finished!")

    # Close the connection.
    response.close()






if __name__ == '__main__':
    with ThreadPoolExecutor(20) as t:

        # 1-200 means 199 pages, and each page have 24 items.
        for i in range(1, 200):
            t.submit(get_fruit_price, f"https://www.guo68.com/market?page={i}")

    print("\nAll Finished.")