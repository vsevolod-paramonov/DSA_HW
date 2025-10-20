import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from traversal.bst import Node, BST
from is_balanced import is_balanced


class TestBalancedBinaryTree(unittest.TestCase):

    def test_empty_tree(self):
        self.assertTrue(is_balanced(None))

    def test_single_node(self):
        n = Node(5)
        self.assertTrue(is_balanced(n))

    def test_two_nodes_left(self):
        n = Node(5)
        n.l = Node(3)
        self.assertTrue(is_balanced(n))

    def test_two_nodes_right(self):
        n = Node(5)
        n.r = Node(7)
        self.assertTrue(is_balanced(n))

    def test_balanced_full_tree(self):
        t = BST()
        for k in [5, 3, 7, 2, 4, 6, 8]:
            t.insert(k)
        self.assertTrue(is_balanced(t.root))

    def test_balanced_small_tree(self):
        n = Node(1)
        n.l = Node(2)
        n.r = Node(3)
        self.assertTrue(is_balanced(n))

    def test_balanced_almost_full(self):

        n = Node(1)
        n.l = Node(2)
        n.r = Node(3)
        n.l.l = Node(4)
        self.assertTrue(is_balanced(n))

    # === НЕСБАЛАНСИРОВАННЫЕ ===
    def test_unbalanced_left(self):
        n = Node(1)
        n.l = Node(2)
        n.l.l = Node(3)
        self.assertFalse(is_balanced(n))

    def test_unbalanced_right(self):
        n = Node(1)
        n.r = Node(2)
        n.r.r = Node(3)
        n.r.r.r = Node(4)
        self.assertFalse(is_balanced(n))

    def test_unbalanced_deep_left(self):
        n = Node(10)
        n.l = Node(5)
        n.l.l = Node(2)
        n.l.l.l = Node(1)
        self.assertFalse(is_balanced(n))

    def test_unbalanced_deep_right(self):
        n = Node(10)
        n.r = Node(20)
        n.r.r = Node(30)
        n.r.r.r = Node(40)
        self.assertFalse(is_balanced(n))

    def test_balanced_with_nulls(self):
        n = Node(1)
        n.l = Node(2)
        n.r = Node(3)
        n.l.l = Node(4)
        self.assertTrue(is_balanced(n))

    def test_unbalanced_asymmetric(self):
        n = Node(1)
        n.l = Node(2)
        n.r = Node(3)
        n.l.l = Node(4)
        n.l.l.l = Node(5)
        self.assertFalse(is_balanced(n))


if __name__ == "__main__":
    unittest.main()
