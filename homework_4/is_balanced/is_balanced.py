from traversal.bst import Node

def is_balanced(root):
    
    def check_one(n):
        if not n:
            return 0, True
        
        lh, left_ok = check_one(n.l)
        rh, right_ok = check_one(n.r)
        
        diff_ok = abs(lh - rh) <= 1
        ok = left_ok and right_ok and diff_ok
        
        return 1 + max(lh, rh), ok

    _, balanced = check_one(root)

    return balanced
