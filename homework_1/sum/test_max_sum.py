import unittest
from max_sum import max_sum_div2

class TestMaxSum(unittest.TestCase):      
    def test_empty(self):
        self.assertEqual(max_sum_div2([]), 0)

    def test_all_even(self):
        self.assertEqual(max_sum_div2([2, 4, 6]), 12)
        self.assertEqual(max_sum_div2([0, 8, 10]), 18)

    def test_all_odd(self):
        self.assertEqual(max_sum_div2([1, 3, 5]), 8)
        self.assertEqual(max_sum_div2([7, 9, 11]), 20)

    def test_mixed_numbers(self):
        self.assertEqual(max_sum_div2([1, 2, 3, 4]), 10)
        self.assertEqual(max_sum_div2([10, 15, 20, 25]), 70)

    def test_no_odd_numbers(self):
        self.assertEqual(max_sum_div2([2, 4, 6, 8]), 20)
        self.assertEqual(max_sum_div2([0, 12, 14]), 26)

    def test_single_element(self):
        self.assertEqual(max_sum_div2([5]), 0)
        self.assertEqual(max_sum_div2([8]), 8)

    
if __name__ == "__main__":
    unittest.main()