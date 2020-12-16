class RBTreeNode:
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'black'


class RBTree:
    def __init__(self):
        self.nil = RBTreeNode(-1)
        self.root = self.nil
