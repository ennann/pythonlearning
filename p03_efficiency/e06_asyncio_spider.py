import requests
import asyncio
import aiohttp
import aiofiles
import json
import time


"""
Request getCatalog to get all the cid of a book.
https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}

Request getChapterContent to download all the contents from the cid.
https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}
"""

#
async def getChapterContent(bookid, cid, title):
    url_data = {
        "book_id":bookid,
        "cid":f"{bookid}|{cid}",
        "need_bookinfo":1
    }

    url_data = json.dumps(url_data)

    url = f'https://dushu.baidu.com/api/pc/getChapterContent?data={url_data}'
    # print(url)
    conn = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(url) as response:
            respjson = await response.json()
            content = respjson["data"]["novel"]["content"]
            async with aiofiles.open(f'/Users/Elton/Code-stuff/pythonlearning/p03_efficiency/Journey to the West/{title}', mode="w", encoding="utf-8") as f:
                await f.write(content)


# Define a function that can get the cid of a book, need provide a bookid.
async def getChapterid(book_id):

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
    }
    book_id = str(book_id)
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + book_id + '"}'

    response = requests.get(url, headers=headers)

    status_code = response.status_code
    if status_code != 200:
        print("You need to check the network connection, may be your IP was blocked.")

    # print(response.json()["data"]["novel"]["items"])
    respjson = response.json()
    items = respjson["data"]["novel"]["items"]

    itemDictionary = {}

    tasks = []

    for item in items:
        chapter_title = item["title"]
        price_status = item["price_status"]
        chapter_id = int(item["cid"])
        itemDictionary[chapter_id] = chapter_title

        # Need to provide async task here.
        tasks.append(getChapterContent(bookid=book_id, cid=chapter_id, title=chapter_title))
    await asyncio.wait(tasks)

# Run
if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(getChapterid(4306063500))
    print(f"Time costs:{time.time()-start_time}")
