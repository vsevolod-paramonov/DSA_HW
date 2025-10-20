class Node:
    def __init__(self, k):
        self.k = k
        self.l = None
        self.r = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, k):
        if not self.root:
            self.root = Node(k)
            return
        cur = self.root
        while True:
            if k < cur.k:
                if cur.l:
                    cur = cur.l
                else:
                    cur.l = Node(k)
                    return
            else:
                if cur.r:
                    cur = cur.r
                else:
                    cur.r = Node(k)
                    return

    ### Прямой обход
    
    def preorder(self):
        res = []
        def go(n):
            if not n: return
            res.append(n.k)
            go(n.l)
            go(n.r)
        go(self.root)
        return res

    def inorder(self):
        res = []
        def go(n):
            if not n: return
            go(n.l)
            res.append(n.k)
            go(n.r)
        go(self.root)
        return res

    def postorder(self):
        res = []
        def go(n):
            if not n: return
            go(n.l)
            go(n.r)
            res.append(n.k)
        go(self.root)
        return res

    ### Обратный обход

    def reverse_preorder(self):
        res = []
        def go(n):
            if not n: return
            res.append(n.k)
            go(n.r)
            go(n.l)
        go(self.root)
        return res

    def reverse_inorder(self):
        res = []
        def go(n):
            if not n: return
            go(n.r)
            res.append(n.k)
            go(n.l)
        go(self.root)
        return res

    def reverse_postorder(self):
        res = []
        def go(n):
            if not n: return
            go(n.r)
            go(n.l)
            res.append(n.k)
        go(self.root)
        return res