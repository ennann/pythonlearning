"""
正整数的反转

Version: 0.1
Author: 骆昊
"""

# 这个方法要比 for 巡检简洁多了

num = 123456
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

test = 124
print(test // 10)  # 向下取整数的意思，向上取证书可以参参考之前的 math 的 celi 库

# 生成斐波那契数列的前20个数。
num_1 = 1
num_2 = 1

for i in range(1, 21):
    if i == 1:
        num_1 = 1
        print(f"The {i}th number is {num_1}")
    elif i == 2:
        num_2 = 1
        print(f"The {i}th number is {num_2}")
    elif i > 2:
        num = num_1 + num_2
        print(f"The {i}th number is {num}")
        num_2, num_1 = num_1, num


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


# 找出10000以内的完美数。

for number in range(1, 10001):
    # 找出真因子
    factors = []
    for n in range(1, number):
        if number % n == 0:
            factors.append(n)

    factors_sum = 0
    for _ in factors:
        factors_sum += _
    if factors_sum == number:
        string = "="
        for ele in factors:
            string = string + " + " + str(ele)
        print(str(number), string)

if __name__ == '__main__':
    main()
