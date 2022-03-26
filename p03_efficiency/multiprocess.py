from multiprocessing import Process

def func(name):
    for i in range(1000):
        print("子进程", name,  i)

if __name__ == '__main__':
    p1 = Process(target=func, args=("No.1 Process",))
    p1.start()
    for i in range(1000):
        print("主进程", i)

