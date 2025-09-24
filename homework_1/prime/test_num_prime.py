

import unittest
from num_prime import num_prime_digits

class TestCountPrimeDigits(unittest.TestCase):

    def dumb_negative_test(self):
        self.assertEqual(num_prime_digits(-10), 0)   

    def test_zero_and_one(self):
        self.assertEqual(num_prime_digits(0), 0)   
        self.assertEqual(num_prime_digits(1), 0)   


    def test_prime_digits(self):
        self.assertEqual(num_prime_digits(17), 7)  
        self.assertEqual(num_prime_digits(5), 3)  
    

    def test_non_prime_digits(self):
        self.assertEqual(num_prime_digits(4), 2)  
        self.assertEqual(num_prime_digits(10), 4)

if __name__ == "__main__":
    unittest.main()