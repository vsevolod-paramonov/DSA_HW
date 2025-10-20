from traversal.bst import Node

def is_valid_bst(root):
    def is_valid_i(n, low, high):

        if not n:
            return True
        
        if not (low < n.k < high):
            return False
        
        return is_valid_i(n.l, low, n.k) and is_valid_i(n.r, n.k, high)
    
    return is_valid_i(root, float('-inf'), float('inf'))
