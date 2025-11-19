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


### MERGE SORT ###

@set_timer
def MergeSort(arr):
    width = 1
    n = len(arr)
    result = arr.copy()

    while width < n:
        for i in range(0, n, width * 2):
            left = result[i : i + width]
            right = result[i + width : i + 2 * width]
            result[i : i + 2 * width] = merge(left, right)
        width *= 2
    return result


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

### QUICK SORT ###

@set_timer
def QuickSort(arr):
    stack = [(0, len(arr) - 1)]
    result = arr.copy()

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(result, low, high)

            if pivot_index - 1 - low > high - (pivot_index + 1):
                stack.append((low, pivot_index - 1))
                stack.append((pivot_index + 1, high))
            else:
                stack.append((pivot_index + 1, high))
                stack.append((low, pivot_index - 1))

    return result


def partition(arr, low, high):
    mid = (low + high) // 2
    pivot = arr[mid]

    arr[mid], arr[high] = arr[high], arr[mid]

    store = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[store] = arr[store], arr[i]
            store += 1

    arr[store], arr[high] = arr[high], arr[store]
    return store