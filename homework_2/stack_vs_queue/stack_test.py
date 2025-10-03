import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def test_push_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

    def test_empty_pop(self):
        stack = Stack()
        self.assertRaises(AssertionError, stack.pop)

    def test_peek(self):
        stack = Stack()
        stack.push(10)
        self.assertEqual(stack.peek(), 10)
        stack.push(20)
        self.assertEqual(stack.peek(), 20)


if __name__ == "__main__":
    unittest.main()