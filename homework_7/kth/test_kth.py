import unittest
import random
from kth import findKthLargest_without_heapq, findKthLargest_heapq

class TestKthLargestMinHeap(unittest.TestCase):
    def setUp(self):
        self.simple = [3, 2, 1, 5, 6, 4]
        self.simple2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        self.all_equal = [42] * 1000
        self.sorted_asc = list(range(1000))
        self.sorted_desc = list(range(1000, 0, -1))
        self.random_big = random.sample(range(10**7), 1000)

    def test_examples(self):
        for func in [findKthLargest_without_heapq, findKthLargest_heapq]:
            self.assertEqual(func(self.simple.copy(), 2), 5)
            self.assertEqual(func(self.simple2.copy(), 4), 4)

    def test_all_equal(self):
        for func in [findKthLargest_without_heapq, findKthLargest_heapq]:
            self.assertEqual(func(self.all_equal.copy(), 50), 42)
            self.assertEqual(func(self.all_equal.copy(), 999), 42)
            self.assertEqual(func(self.all_equal.copy(), 1), 42)

    def test_sorted(self):
        for func in [findKthLargest_without_heapq, findKthLargest_heapq]:
            self.assertEqual(func(self.sorted_asc.copy(), 1), 999)
            self.assertEqual(func(self.sorted_asc.copy(), 1000), 0)
            self.assertEqual(func(self.sorted_asc.copy(), 500), 500)

    def test_reverse_sorted(self):
        for func in [findKthLargest_without_heapq, findKthLargest_heapq]:
            self.assertEqual(func(self.sorted_desc.copy(), 1), 1000)
            self.assertEqual(func(self.sorted_desc.copy(), 1000), 1)
            self.assertEqual(func(self.sorted_desc.copy(), 500), 501)

    def test_one_element(self):
        for func in [findKthLargest_without_heapq, findKthLargest_heapq]:
            self.assertEqual(func([17],1), 17)

    def test_random_big(self):
        k = 10
        answer = sorted(self.random_big)[-k]
        for func in [findKthLargest_without_heapq, findKthLargest_heapq]:
            self.assertEqual(func(self.random_big.copy(), k), answer)


if __name__ == "__main__":
    unittest.main()