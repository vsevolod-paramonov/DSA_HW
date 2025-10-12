import unittest
from anagrams import anagrams


class TestAnagrams(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(anagrams([]), [])

    def test_single_word(self):
        self.assertEqual(anagrams(["abc"]), [["abc"]])

    def test_duplicates(self):
        words = ["abc", "bca", "cab", "abc"]
        result = anagrams(words)
        expected = [["abc", "bca", "cab", "abc"]]
        self.assertCountEqual([sorted(g) for g in result], [sorted(g) for g in expected])

    def test_no_anagrams(self):
        words = ["dog", "cat", "bird"]
        result = anagrams(words)
        expected = [["dog"], ["cat"], ["bird"]]
        self.assertCountEqual([sorted(g) for g in result], [sorted(g) for g in expected])


if __name__ == "__main__":
    unittest.main()
