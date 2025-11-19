import unittest
import random
from kth import findKthLargest  


class TestKthLargest(unittest.TestCase):
    def setUp(self):
        self.small_list = [3, 2, 1, 5, 6, 4]
        self.small_list2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]

        self.sorted_list = list(range(100000))
        self.reversed_list = list(range(100000))[::-1]

    def test_examples(self):
        self.assertEqual(findKthLargest(self.small_list.copy(), 2), 5)
        self.assertEqual(findKthLargest(self.small_list2.copy(), 4), 4)


    def test_sorted_input(self):
        k = 100
        expected = self.sorted_list[-k]
        result = findKthLargest(self.sorted_list.copy(), k)

        self.assertEqual(result, expected)

    def test_reversed_input(self):
        k = 50
        expected = sorted(self.reversed_list)[-k]
        result = findKthLargest(self.reversed_list.copy(), k)

        self.assertEqual(result, expected)

    def test_all_equal(self):
        nums = [7] * 1000
        for k in (1, 10, 500, 999):
            self.assertEqual(findKthLargest(nums.copy(), k), 7)

    def test_single_element(self):
        nums = [42]
        self.assertEqual(findKthLargest(nums.copy(), 1), 42)


if __name__ == "__main__":
    unittest.main()