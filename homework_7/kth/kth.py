
import heapq


def min_sift_down(heap, size, i):
    while 2*i+1 < size:
        l, r = 2*i+1, 2*i+2
        j = l
        if r < size and heap[r] < heap[l]:
            j = r
        if heap[i] <= heap[j]:
            break
        heap[i], heap[j] = heap[j], heap[i]
        i = j

def min_sift_up(heap, i):
    while i > 0:
        p = (i-1)//2
        if heap[i] >= heap[p]:
            break
        heap[i], heap[p] = heap[p], heap[i]
        i = p

def findKthLargest_without_heapq(nums, k):
    heap = []
    for num in nums:
        if len(heap) < k:
            heap.append(num)
            min_sift_up(heap, len(heap)-1)
        else:
            if num > heap[0]:
                heap[0] = num
                min_sift_down(heap, k, 0)
    return heap[0]


### with heapq

def findKthLargest_heapq(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappushpop(heap, num)
    return heap[0]