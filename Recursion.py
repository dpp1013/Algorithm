'''
递归算法实现货币兑换
要求：兑换的钱币数量最少
结束条件：需要兑换的找零，其面值正好等于某种硬币
减小问题的规模：我们要对每种硬币尝试一次，例如美元硬币体系：
    1.找零减去1分后，求兑换硬币最少数量（递归调用自身）
    2.找零减去5分后，求兑换硬币最少数量
    3.找零减去10分后，求兑换硬币最少数量
    4.找零25分后，求兑换硬币最少数量
    上述四项中选择最小的一个
'''
import time
import numpy as np


def reMC(coinValueList, change):
    '''
    :param coinValueList: 货币列表，minCoin 最小兑换次数
    :param change: 兑换的钱
    :return: 兑换的次数
    '''
    minCoin = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c < change]:
            numCoin = 1 + reMC(coinValueList, change - i)
        if minCoin > numCoin:
            minCoin = numCoin
    return minCoin


'''
递归优化，对于这个递归算法进行改进的关键在于消除重复计算。我们可以用一个表将计算过的中间结果保存起来，在计算之前查表看看
是否已经计算过。
这个算法的中间结果就是部分找零的最优解，在递归调用过程中已经得到的最优解被记录下来。
在递归调用之前，先查找表中是否已有部分找零的最优解，如果有，直接返回最优解而不进行递归调用
如果没有，才进行递归调用
'''


# 这种方法叫memorization(记忆化/函数值缓存)

def reMC2(coinValueList, change, knownResult):
    '''
    :param coinValueList: 货币
    :param change: 要兑换的钱
    :param knownResult: 已有的最优解,换change时的最小硬币是多少
    :return: 兑换次数
    '''
    result = []
    minCoin = change
    if change in coinValueList:
        return 1
    elif knownResult[change] > 0:
        return knownResult[change]  # 查表成功，直接用最优解
    else:
        for i in [c for c in coinValueList if c < change]:
            numCoin = 1 + reMC2(coinValueList, change - i, knownResult)
            if numCoin < minCoin:
                minCoin = numCoin
                # 保存已有的最优解，
                knownResult[change] = minCoin
        return minCoin


def Fibonacci(n):
    '''
    用循环解
    '''
    first = 1
    second = 1
    print(first, second, end='\t')
    for i in range(n - 2):
        third = first + second
        print(third, end=' ')
        first = second
        second = third


def FibonacciRecurision(n):
    '''
    用递归解
    1.递归的结束条件n=1时，直接返回本身就行了
    2. 问题的规模逐渐变小
    3.调用自身
    '''
    if n == 1 or n == 0:
        return 1
    else:
        return FibonacciRecurision(n - 1) + FibonacciRecurision(n - 2)


if __name__ == '__main__':
    print(reMC([1, 5, 10, 25], 26))
    print(reMC2([1, 5, 10, 25], 26, [0] * 27))
