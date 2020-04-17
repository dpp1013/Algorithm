'''
选择排序
每趟都使当前最大项就位
但选择排序对交换进行削减，相比起冒泡排序进行多次交换，每趟仅进行1次
交换，记录最大项的所在位置，最后再跟本趟最后一项交换
选择排序的时间复杂度比冒泡排序稍优
- 对比次数不变O(n*n)
- 交换次数则减少为O(n)
'''


def selection(lists):
    for i in range(len(lists) - 1, 0, -1):
        max = 0
        for j in range(0, i+1):
            if lists[j] > max:
                max = lists[j]
        index = lists.index(max)
        swapt = lists[index]
        lists[index] = lists[i]
        lists[i] = swapt
    return lists


if __name__ == '__main__':
    print(selection([3, 6, 8, 10, 13, 16]))
