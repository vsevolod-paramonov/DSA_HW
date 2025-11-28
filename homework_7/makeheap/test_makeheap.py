
import unittest
import random
import time
from makeheap import makeheap, makeheap_n_log_n

def is_minheap(arr):
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True

class TestHeapBuilding(unittest.TestCase):
    def setUp(self):
        self.example = [3, 1, 4, 1, 5, 9, 2, 6]
        self.duplicates = [2, 2, 2, 2, 2, 2, 2]
        self.sorted_asc = list(range(1000))
        self.sorted_desc = list(range(1000))[::-1]
        self.randomized = random.sample(range(10000), 1000)

    def test_example_heap(self):
        arr = self.example.copy()
        makeheap(arr)
        self.assertTrue(is_minheap(arr))
        arr2 = self.example.copy()
        makeheap_n_log_n(arr2)
        self.assertTrue(is_minheap(arr2))

    def test_duplicates(self):
        for func in (makeheap, makeheap_n_log_n):
            arr = self.duplicates.copy()
            func(arr)
            self.assertTrue(is_minheap(arr))

    def test_sorted_input(self):
        for func in (makeheap, makeheap_n_log_n):
            arr = self.sorted_asc.copy()
            func(arr)
            self.assertTrue(is_minheap(arr))

    def test_reverse_sorted_input(self):
        for func in (makeheap, makeheap_n_log_n):
            arr = self.sorted_desc.copy()
            func(arr)
            self.assertTrue(is_minheap(arr))

    def test_empty(self):
        arr = []
        for func in (makeheap, makeheap_n_log_n):
            arr_copy = arr.copy()
            func(arr_copy)
            self.assertTrue(is_minheap(arr_copy))

    def test_one_element(self):
        arr = [42]
        for func in (makeheap, makeheap_n_log_n):
            arr_copy = arr.copy()
            func(arr_copy)
            self.assertTrue(is_minheap(arr_copy))

    def test_performance(self):
        big = random.sample(range(10**10), 10**6) 
        for name, func in [("makeheap", makeheap), 
                           ("makeheap_n_log_n", makeheap_n_log_n)]:
            arr = big.copy()
            start = time.time()
            func(arr)
            elapsed = time.time() - start
            print(f"{name} took {elapsed:.4f} seconds")
            self.assertTrue(is_minheap(arr))


if __name__ == "__main__":
    unittest.main()