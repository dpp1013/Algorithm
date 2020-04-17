'''
二分查找
'''


def binary(lists, num):
    found = False
    start = 0
    end = len(lists) - 1
    while end >= start and not found:
        print("start=", start)
        print("end=", end)
        middle = (start + end) // 2
        print(middle)
        if num == lists[middle]:
            found = True
            return found
        elif num > lists[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return found


# 递归求解
def recursionBinary(lists, num):
    # 递归结束条件
    if len(lists) == 0:
        return False
    else:
        midpoint = len(lists) // 2
        if num > lists[midpoint]:
            return recursionBinary(lists[midpoint + 1:], num)
        elif num < lists[midpoint]:
            return recursionBinary(lists[:midpoint - 1], num)
        else:
            return True

if __name__ == '__main__':
    print(recursionBinary([10, 11,12,15], 10))
