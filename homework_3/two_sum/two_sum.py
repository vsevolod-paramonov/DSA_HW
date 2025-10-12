def two_sum(nums, target):

    hashMap = dict()

    for i in range(len(nums)):
        if nums[i] in hashMap:
            return [i, hashMap[nums[i]]]
        else:
            hashMap[target - nums[i]] = i