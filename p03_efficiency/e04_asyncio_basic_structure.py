import asyncio
import time

async def func1():
    print("This is test 1.1")
    await asyncio.sleep(3)
    print("This is test 1.2")


async def func2():
    print("This is test 2.1")
    await asyncio.sleep(5)
    print("This is test 2.2")


async def func3():
    print("This is test 3.1")
    await asyncio.sleep(2)
    print("This is test 3.2")


# Method one:
# if __name__ == '__main__':
#     f1 = func1()
#     f2 = func2()
#     f3 = func3()
#
#     tasks = [f1, f2, f3]
#
#     start_time = time.time()
#     asyncio.run(asyncio.wait(tasks))
#     end_time = time.time()
#     print(f"Time costs:{end_time-start_time}")


# Method two:
async def main():
    tasks = [
        func1(),
        func2(),
        func3()
    ]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print(f"Time costs:{time.time()-start_time}")