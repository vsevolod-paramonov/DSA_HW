import unittest
from merge_lists import ListNode, merge_lists_with_dummy, merge_lists_without_dummy


def list_to_linked(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linked_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


class TestMergeLists(unittest.TestCase):

    def check_both(self, list1, list2, expected):
        l1 = list_to_linked(list1)
        l2 = list_to_linked(list2)
        res1 = merge_lists_with_dummy(l1, l2)
        self.assertEqual(linked_to_list(res1), expected)

        l1 = list_to_linked(list1)
        l2 = list_to_linked(list2)
        res2 = merge_lists_without_dummy(l1, l2)
        self.assertEqual(linked_to_list(res2), expected)

    def test_normal_case(self):
        self.check_both([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])

    def test_one_empty(self):
        self.check_both([], [0], [0])

    def test_both_empty(self):
        self.check_both([], [], [])

    def test_different_lengths(self):
        self.check_both([1, 2, 3], [4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8])

    def test_duplicates(self):
        self.check_both([2, 2, 2], [2, 2], [2, 2, 2, 2, 2])


if __name__ == "__main__":
    unittest.main()
