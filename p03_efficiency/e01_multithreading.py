from threading import Thread

# def func():
#     for i in range(1000):
#         print("func", i)
#
# if __name__ == '__main__':
#     t = Thread(target=func)
#     # 在此我犯了一个错误，我把 func 加上了空格，导致一直执行完毕才进行下一行。
#     t.start()
#     for i in range(1000):
#         print("main", i)

class MyThread(Thread):
    def run(self):
        for i in range(1000):
            print("子线程", i)

if __name__ == '__main__':
    t1 = MyThread()
    t1.start()

    for i in range(1000):
        print("主线程", i)

