import unittest
from avl import AVL

class TestAVL(unittest.TestCase):
    def test_insert_search(self):
        tree = AVL()
        tree.insert(10)
        tree.insert(20)
        tree.insert(5)

        self.assertTrue(tree.search(10))
        self.assertTrue(tree.search(20))
        self.assertTrue(tree.search(5))
        self.assertFalse(tree.search(15))

    def test_delete_leaf(self):
        tree = AVL()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        tree.delete(5)
        self.assertFalse(tree.search(5))
        self.assertTrue(tree.search(10))
        self.assertTrue(tree.search(15))

    def test_delete_node_with_one_child(self):
        tree = AVL()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        tree.insert(12)
        tree.delete(15)
        self.assertFalse(tree.search(15))
        self.assertTrue(tree.search(12))

    def test_delete_node_with_two_children(self):
        tree = AVL()
        for x in [20, 10, 30, 5, 15, 25, 35]:
            tree.insert(x)
        tree.delete(20)
        self.assertFalse(tree.search(20))
        self.assertEqual(tree.inorder(), [5, 10, 15, 25, 30, 35])

    def test_inorder(self):
        tree = AVL()
        for x in [3, 1, 2, 5, 4]:
            tree.insert(x)
        self.assertEqual(tree.inorder(), [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main()
