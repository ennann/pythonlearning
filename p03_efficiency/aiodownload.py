import asyncio
import certifi
import aiohttp

urls = [
    "http://kr.shanghai-jiuxin.com/file/2022/0303/a8465844aa1baec67a4b90355659974b.jpg",
    "http://kr.shanghai-jiuxin.com/file/2022/0303/8bf6183877c13df3b1916b6e63c63894.jpg",
    "http://kr.shanghai-jiuxin.com/file/2022/0303/48478fa27485b6a5e4a17c08d6bf1cca.jpg",
    "http://kr.shanghai-jiuxin.com/file/2022/0303/f5bb8caf88e3072cb157481bcb488d50.jpg"
]


async def aiodownload(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    }
    name = url.rsplit("/", 1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            with open(name, mode="wb") as f:
                f.write(await response.content.read())
    print("1 picture downloaded.")


async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
