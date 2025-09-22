import unittest
from palindrome.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):        

    def test_zero(self):
        self.assertTrue(is_palindrome(0))

    def test_digits(self):
        self.assertTrue(is_palindrome(1))
        self.assertTrue(is_palindrome(2))
        self.assertTrue(is_palindrome(3))
        self.assertTrue(is_palindrome(4))
        self.assertTrue(is_palindrome(5))

    def test_negative_number(self):
        self.assertFalse(is_palindrome(-1))
        self.assertFalse(is_palindrome(-10))
        self.assertFalse(is_palindrome(-22))
        self.assertFalse(is_palindrome(-131))

    def test_palindromes(self):
        self.assertTrue(is_palindrome(11))
        self.assertTrue(is_palindrome(121))
        self.assertTrue(is_palindrome(1221))
        self.assertTrue(is_palindrome(12321))
        self.assertTrue(is_palindrome(1234321))



if __name__ == "__main__":
    unittest.main()