'''
动态规划算法采用了一种更有条理的方式得到问题的解
找零兑换的动态规划算法从最简单的“1分钱找零”的最优解开始，逐步递加上去，直到我们需要的找零钱数
在找零递加的过程中，设法保持每一分钱的递加都是最优解，一直加到求解找零钱数，自然得到最优解

递加的过程能保持最优解的关键是，其依赖于更少钱数最优解的简单计算，而更少钱数的最优解已经得到了
问题的最优解包含了更小规模自问题的最优解，这是一个最优化问题能够用动态规划策略解决的必要条件
'''
'''
动态规划的最主要思想：
从最简单情况开始达到所需要找零的循环，其每一步都依靠以前的最优解来得到本步骤的最优解，知道得到答案
'''

def dpMakeChange(coinValueList, change, minCoins):
    # 从1分开始到change逐个计算最少硬币
    for cents in range(1, change + 1):
        # 1.初始化一个最大值
        coinCount = cents  # coinCount 硬币数量
        # 2. 减去每个硬币，向后查最少硬币数，同时记录总的最少数
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
        # 3.得到当前最少硬币数，记录到表中
        minCoins[cents] = coinCount
    # 返回最后一个结果
    return minCoins[change]


if __name__ == '__main__':
    print(dpMakeChange([1, 2, 3, 4], 23, [0] * 24))
