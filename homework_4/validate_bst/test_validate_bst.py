import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from traversal.bst import Node, BST
from validate_bst import is_valid_bst


class TestValidateBST(unittest.TestCase):

    def test_empty_tree(self):
        self.assertTrue(is_valid_bst(None))

    def test_single_node(self):
        n = Node(10)
        self.assertTrue(is_valid_bst(n))

    def test_valid_tree_balanced(self):
        t = BST()
        for k in [5, 3, 7, 2, 4, 6, 8]:
            t.insert(k)
        self.assertTrue(is_valid_bst(t.root))

    def test_valid_tree_unbalanced_left(self):
        t = BST()
        for k in [10, 5, 2, 1]:
            t.insert(k)
        self.assertTrue(is_valid_bst(t.root))

    def test_valid_tree_unbalanced_right(self):
        t = BST()
        for k in [1, 2, 3, 4]:
            t.insert(k)
        self.assertTrue(is_valid_bst(t.root))

    def test_invalid_left_violation(self):
        n = Node(5)
        n.l = Node(8)
        self.assertFalse(is_valid_bst(n))

    def test_invalid_right_violation(self):
        n = Node(5)
        n.r = Node(3)
        self.assertFalse(is_valid_bst(n))

    def test_invalid_deep_violation(self):
        n = Node(10)
        n.l = Node(5)
        n.r = Node(15)
        n.r.l = Node(6)
        self.assertFalse(is_valid_bst(n))

    def test_duplicate_values(self):
        n = Node(5)
        n.l = Node(3)
        n.r = Node(5)
        self.assertFalse(is_valid_bst(n))

    def test_negative_values_valid(self):
        t = BST()
        for k in [0, -10, 10, -20, -5, 5, 20]:
            t.insert(k)
        self.assertTrue(is_valid_bst(t.root))

    def test_invalid_with_same_value_left(self):
        n = Node(5)
        n.l = Node(5)
        self.assertFalse(is_valid_bst(n))

    def test_invalid_with_same_value_right(self):
        n = Node(5)
        n.r = Node(5)
        self.assertFalse(is_valid_bst(n))


if __name__ == "__main__":
    unittest.main()
