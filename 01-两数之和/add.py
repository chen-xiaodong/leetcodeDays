def two_sum(nums, target):
    """这样写更直观，遍历列表同时查字典"""
    dct = {}
    for i, n in enumerate(nums):
        if target - n in dct:
            return [dct[target - n], i]
        dct[n] = i

if __name__ == '__main__':
    num = [3, 3]
    target = 6
    twoSum(num, target)
