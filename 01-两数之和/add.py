def two_sum(nums, target):
    """这样写更直观，遍历列表同时查字典"""
    # 创建一个空白字典
    dct = {}
    # 循环开始
    for i, n in enumerate(nums):
        # 判断结果是否在这字典中
        if target - n in dct:
            return [dct[target - n], i]
        # 这句话放在最后为了避免有重复值 即target-n=n的情况
        dct[n] = i
