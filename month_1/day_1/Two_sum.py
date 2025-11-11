def two_sum_upgraded(nums, target):
    a = {}
    for i in range(len(nums)):
        x = target - nums[i]
        if x in a:
            return [i, a[x]]
        a[nums[i]] = i    