import unittest
from two_sum import two_sum


class TestTwoSum(unittest.TestCase):

    def test_no_solution(self):
        nums = [1, 2, 3]
        target = 7
        result = two_sum(nums, target)
        self.assertIsNone(result, "None, т.к. нет пары")

    def test_example_case(self):
        nums = [2, 7, 11, 15]
        target = 9
        result = two_sum(nums, target)
        self.assertCountEqual(result, [0, 1])

    def test_multiple_pairs(self):
        nums = [3, 2, 4]
        target = 6
        result = two_sum(nums, target)
        self.assertCountEqual(result, [1, 2])

    def test_negative_numbers(self):
        nums = [-3, 4, 3, 90]
        target = 0
        result = two_sum(nums, target)
        self.assertCountEqual(result, [0, 2])

    def test_same_number_twice(self):
        nums = [3, 3]
        target = 6
        result = two_sum(nums, target)
        self.assertCountEqual(result, [0, 1])


if __name__ == "__main__":
    unittest.main()
