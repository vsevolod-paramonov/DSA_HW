from bst import BST

import unittest

class TestBSTTraversal(unittest.TestCase):
    def setUp(self):
        self.t = BST()
        for k in [5, 3, 7, 2, 4, 6, 8]:
            self.t.insert(k)

    def test_preorder(self):
        self.assertEqual(self.t.preorder(), [5, 3, 2, 4, 7, 6, 8])

    def test_inorder(self):
        self.assertEqual(self.t.inorder(), [2, 3, 4, 5, 6, 7, 8])

    def test_postorder(self):
        self.assertEqual(self.t.postorder(), [2, 4, 3, 6, 8, 7, 5])

    def test_reverse_preorder(self):
        self.assertEqual(self.t.reverse_preorder(), [5, 7, 8, 6, 3, 4, 2])

    def test_reverse_inorder(self):
        self.assertEqual(self.t.reverse_inorder(), [8, 7, 6, 5, 4, 3, 2])

    def test_reverse_postorder(self):
        self.assertEqual(self.t.reverse_postorder(), [8, 6, 7, 4, 2, 3, 5])

if __name__ == "__main__":
    unittest.main()