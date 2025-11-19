import time

def set_timer(fn):
    def wrap(*args, **kwargs):
        if getattr(fn, "_running", False): 
            return fn(*args, **kwargs)
        fn._running = True

        start_time = time.time()

        result = fn(*args, **kwargs)

        end_time = time.time()
        fn._running = False
        print(f"{fn.__name__} run took {end_time - start_time:.2f} sec")
        return result
    return wrap

### MERGE SORT (ITERATIVE) ###

def merge(l, r):
    output = []
    i = j = 0

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            output.append(l[i])
            i += 1
        else:
            output.append(r[j])
            j += 1

    output += l[i:]
    output += r[j:]
    return output


@set_timer
def MergeSort(nums):
    n = len(nums)
    width = 1
    nums = nums.copy()

    while width < n:
        for i in range(0, n, width * 2):
            l = nums[i : i + width]
            r = nums[i + width : i + width * 2]
            nums[i : i + width * 2] = merge(l, r)
        width *= 2

    return nums

## QUICK SORT (ITERATIVE) ###

def partition(nums, low, high):
    mid = (low + high) // 2
    pivot = nums[mid]

    nums[mid], nums[high] = nums[high], nums[mid]

    store = low
    for i in range(low, high):
        if nums[i] < pivot:
            nums[i], nums[store] = nums[store], nums[i]
            store += 1

    nums[store], nums[high] = nums[high], nums[store]
    return store



@set_timer
def QuickSort(nums):
    nums = nums.copy()
    stack = [(0, len(nums) - 1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            p = partition(nums, low, high)

            if p - 1 - low > high - (p + 1):
                stack.append((low, p - 1))
                stack.append((p + 1, high))
            else:
                stack.append((p + 1, high))
                stack.append((low, p - 1))

    return nums
