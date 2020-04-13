'''
冒泡排序时间复杂度O(n*n)
时间复杂度较差，其效率主要差在每个数据项在找到最终位置之前，必须要经过多次对比和交换，其中大部分的操作是无效的。
但是有一点优势，就是无需任何额外的存储空间消耗。
另外，通过监测每趟对比是否发生过交换，可以提前确定排序是否完成
这也是其他多数排序算法无法做到的
如果某趟对比没有发生任何交换，说明列表已经排好序，可以提前结束算法。
'''


def buble(lists):
    for i in range(len(lists) - 1, 0, -1):
        for j in range(0, i):
            if lists[j] > lists[j + 1]:
                swapt = lists[j + 1]
                lists[j + 1] = lists[j]
                lists[j] = swapt
    return lists


def improveBuble(lists):
    exchange = True
    passnum = len(lists) - 1
    while passnum > 0 and exchange:
        exchange = False
        for j in range(0, passnum):
            if lists[j] > lists[j + 1]:
                exchange = True
                swapt = lists[j + 1]
                lists[j + 1] = lists[j]
                lists[j] = swapt
        passnum -= 1

    return lists


if __name__ == '__main__':
    print(buble([3, 4, 20, 7, 1, 2, 11, 19]))
