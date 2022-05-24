"""
简单的说，类是对象的蓝图和模板，而对象是类的实例。这个解释虽然有点像用概念在解释概念，但是从这句话我们至少可以看出，类是抽象的概念，而对象是具体的东西。在面向对象编程的世界中，一切皆为对象，对象都有属性和行为，每个对象都是独一无二的，而且对象一定属于某个类（型）。当我们把一大堆拥有共同特征的对象的静态特征（属性）和动态特征（行为）都抽取出来后，就可以定义出一个叫做“类”的东西。

具象化之前就是类
具象化之后就是对象

汽车作为一个分类，他就是类
伊兰特这个车就是一个实例（已经具象化了）
我现在要去开车，「开」就是对实例的操作。

空调 ——> 我的房间的那个空调 ——> 打开空调
汽车设计图 ——> 造出一辆汽车 ——> 造出不同颜色的汽车

定义一个类就相当于写了一个设计图，如果不调用这个类就没有任何意义。
那说明是类的调用？什么是类的具象化？
其实就是那个赋值：
class Person:
    pass

person_1 = Person()
这就是类的具象化，和调用。

其实在之前已经解除到了类了。
比如说这个list 就是一个对象，然后创建一个列表之后就是具象化了一个对象，变成了实例
当你对这个列表进行 append 时，就是对实例的一个操作。

class list(object)
 |  list(iterable=(), /)
 |
 |  Built-in mutable sequence.


"""
from time import sleep


class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')  # 这个就是实例化
    # AttributeError: 'Test' object has no attribute '__bar'
    # test.__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    # print(test.__foo)


if __name__ == "__main__":
    main()


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法

        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    clock = Clock(23, 59, 58)  # 这个就是实例化
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


print(help(list))

# 类的继承
