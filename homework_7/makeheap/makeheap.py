
### nlogn
def sift_up(arr, idx):
    while idx > 0:
        parent = (idx - 1) // 2
        if arr[idx] < arr[parent]:
            arr[idx], arr[parent] = arr[parent], arr[idx]
            idx = parent
        else:
            break

def makeheap_n_log_n(arr):
    heap = []
    for el in arr:
        heap.append(el)
        sift_up(heap, len(heap) - 1)
    arr[:] = heap



### n
def sift_down(arr, n, i):
    while 2 * i + 1 < n:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right
        if smallest == i:
            break
        arr[i], arr[smallest] = arr[smallest], arr[i]
        i = smallest

def makeheap(arr):
    n = len(arr)
    for i in reversed(range(n // 2)):
        sift_down(arr, n, i)