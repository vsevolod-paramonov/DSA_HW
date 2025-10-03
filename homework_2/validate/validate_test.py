import unittest
from validate import validate

class TestValidate(unittest.TestCase):

    def test_case_true(self):
        self.assertTrue(validate([1, 2, 3, 4, 5], [1, 3, 5, 4, 2]))

    def test_case_false(self):
        self.assertFalse(validate([1, 2, 3], [3, 1, 2]))

    def test_single_element(self):
        self.assertTrue(validate([1], [1]))

    def test_empty_both(self):
        self.assertTrue(validate([], []))  

    def test_empty_pushed_nonempty_popped(self):
        self.assertFalse(validate([], [1]))  

    def test_nonempty_pushed_empty_popped(self):
        self.assertFalse(validate([1], []))

if __name__ == "__main__":
    unittest.main()