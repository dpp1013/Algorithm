def threeNum(nums):
    result = []
    if len(nums) < 3:
        return []
    elif len(nums) == 3:
        if sum(nums) == 0:
            return nums
    else:
        nums.sort()
    for i in range(0, len(nums) - 1):
        if nums[i] > 0:
            return result
        L = i + 1
        R = len(nums) - 1
        while L < R:
            if nums[i] + nums[L] + nums[R] == 0:
                result.append([nums[i], nums[L], nums[R]])
                while (L < R and nums[L] == nums[L + 1]):
                    L = L + 1
                while (L < R and nums[R] == nums[R - 1]):
                    R = R - 1
                break
            elif nums[i] + nums[L] + nums[R] > 0:
                R = R - 1
            else:
                L = L + 1
    return result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeNum(nums))
