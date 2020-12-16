import unittest
from RBTree import RBTreeNode, RBTree, Solution


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

    # вставка корня дерева
    def test_tree_insert_root(self):
        rb_tree = RBTree()
        rb_node = RBTreeNode(9)
        sol = Solution()
        sol.RBInsert(rb_tree, rb_node)
        self.assertEqual(rb_tree.root.key, rb_node.key)


if __name__ == '__main__':
    unittest.main()
