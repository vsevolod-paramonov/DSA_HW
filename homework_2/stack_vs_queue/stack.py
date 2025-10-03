class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):

        new_node = ListNode(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):

        assert self.top is not None, "Stack is empty"

        value = self.top.val
        self.top = self.top.next
        return value
    

    def peek(self):

        assert self.top is not None, "Stack is empty"

        return self.top.val