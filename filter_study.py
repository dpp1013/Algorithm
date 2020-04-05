'''
用filter函数求解质数思路：
step1.给定[2,3,4,5,6,7,...]
step2.当i=2时候，用filter过滤到能被2整数的留下[3,5,7,9,...]
step3.取列表的第一个元素，用filter过滤能被该元素整数的数
'''
import numpy as np


# 构造一个生成器
def date_iter():
    n = 1
    while True:
        n = n + 1
        yield n


# 构造一个从3开始的奇数数列,生成器，有很多很多
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 筛选函数,传入的参数是n，除数
def _not_div(n):
    return lambda x: x % n > 0


# 定义一个素数不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter()  # 从3开始的奇数,it是个生成器，包含了一组数据
    while True:
        n = next(it)  # n取奇数生成器的第一个元素
        yield n  # 记住取的位置
        it = filter(_not_div(n), it)  #


# 回文数字
def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':
    # result = primes()
    # for n in primes():
    #     if n < 10:
    #         print('测试', end='\t')
    #     else:
    #         break
    output = filter(is_palindrome, np.arange(1, 100, 1))
    print(list(output))
