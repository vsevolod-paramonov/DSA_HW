import unittest
from permutations import permutations

class TestPermutations(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(permutations([1]), [[1]])

    def test_two_elements(self):
        self.assertEqual(sorted(permutations([0, 1])), sorted([[0, 1], [1, 0]]))
        self.assertEqual(sorted(permutations([1, 2])), sorted([[1, 2], [2, 1]]))

    def test_three_elements(self):
        true_answers = [[1, 2, 3], [1, 3, 2],
                        [2, 1, 3], [2, 3, 1],
                        [3, 1, 2], [3, 2, 1]]
        self.assertEqual(sorted(permutations([1, 2, 3])), sorted(true_answers))


    def test_empty_list(self):
        self.assertEqual(permutations([]), [])

if __name__ == "__main__":
    unittest.main()
