class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def add_to_queue(self, value): 

        new_node = ListNode(value)
        if self.rear is None:  
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def delete_from_queue(self):  

        if self.front is None:  
            return None
        
        value = self.front.val
        self.front = self.front.next

        if self.front is None:  
            self.rear = None
        return value
    
    def peek(self):

        assert self.front is None, "Queue is empty"
        
        return self.front.val
