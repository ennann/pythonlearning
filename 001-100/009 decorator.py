"""
在 Python 中，任何东西都是对象，一个变量、一个函数、一个东……都是对象
你可以调用所有的对象，但是如果一个对象不是 callable，那么就会出 RUN TIME 的错误。

函数既然是对象，对象又可以被调用，
那么说明函数可以被其他的函数调用，并且是当做参数去调用，同时一个函数也可以返回一个函数。

decorator 的使用：
第一种是 @dec 加到一个函数的前面
第二字是直接 deco = dec(func)
两种是完全等价的。




语法糖
wrapper(*args, **kwargs)
中的 *args, **kwargs 是为了能让参数的数量不一的函数，仍然可以使用这个 decorator

有些 decorator 还会带有参数。
函数装饰器 类装饰器。




此外，在一个类中，可以使用静态方法 和 类方法
和静态方法比较类似，Python还可以在类中定义类方法，类方法的第一个参数约定名为cls，它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象），通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象，代码如下所示。


简单的说，类和类之间的关系有三种：is-a、has-a和use-a关系。
is-a 是继承关系
has-a关系通常称之为关联
use-a是依赖关系


https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/res/uml-components.png


什么是抽象类？


"""

import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        print(f"The total time consume is: {time.time() - start}")
        return ret

    return wrapper


@timeit
def test_func(t):
    time.sleep(t)


test_func(1)


class Person(object):
    """
    Person
    """

    # 初始化
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def gender(self):
        return self.gender

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在愉快的玩耍.' % self._name)  # 比较老的编写方法，建议改为下方的最新版。

    def watch_movie(self):
        if self._age >= 18:
            print(f'{self._name}正在观看电影.')
        else:
            print(f'{self._name}只能观看《熊出没》.')


class Student(Person):
    """学生"""

    # 初始化里有几个变量，就要在实例化的时候输入几个变量。
    def __init__(self, name, age, gender, grade):
        super().__init__(name, age, gender)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, gender, title):
        super().__init__(name, age, gender)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))


def main():
    stu = Student('王大锤', 15, 'Male', "12th")
    stu.study('数学')
    stu.watch_movie()

    t = Teacher("王老师", 54, "Male", "Doctor")
    t.teach("Battery")
    t.watch_movie()
    # t = Teacher('骆昊', 38, '砖家')
    # t.teach('Python程序设计')
    # t.watch_movie()


if __name__ == '__main__':
    main()
