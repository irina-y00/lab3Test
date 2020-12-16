import unittest
from RBTree import RBTreeNode, RBTree


class RbTreeTests(unittest.TestCase):

    # инициализация узла дерева
    def test_node_init(self):
        nil = RBTreeNode(15)
        self.assertEqual(nil.key, 15)
        self.assertIsNone(nil.left, None)
        self.assertIsNone(nil.right, None)
        self.assertIsNone(nil.parent, None)
        self.assertEqual(nil.color, 'black')

    # инициализация дерева
    def test_tree_init(self):
        nil = RBTreeNode(-1)
        rb_tree = RBTree()
        self.assertEqual(rb_tree.root.key, nil.key)


if __name__ == '__main__':
    unittest.main()
