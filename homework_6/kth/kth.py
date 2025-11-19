def partition(nums, l, r):
        pivot = nums[(l + r) // 2]
        nums[(l + r) // 2], nums[r] = nums[r], nums[(l + r) // 2]

        store = l

        for i in range(l, r):

            if nums[i] < pivot:
                nums[i], nums[store] = nums[store], nums[i]
                store += 1

        nums[store], nums[r] = nums[r], nums[store]
        return store

def findKthLargest(nums, k):
    k = len(nums) - k 

    l, r = 0, len(nums) - 1

    while True:
        p = partition(nums, l, r)
        
        if p == k:
            return nums[p]
        elif p < k:
            l = p + 1
        else:
            r = p - 1
