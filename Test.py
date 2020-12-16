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

    # вставка левого узла дерева
    def test_tree_insert_left_node(self):
        rb_tree = RBTree()
        rb_node = RBTreeNode(9)
        rb_node_left = RBTreeNode(6)
        sol = Solution()
        sol.RBInsert(rb_tree, rb_node)
        sol.RBInsert(rb_tree, rb_node_left)
        self.assertEqual(rb_tree.root.left.key, rb_node_left.key)

    # вставка правого узла дерева
    def test_tree_insert_right_node(self):
        rb_tree = RBTree()
        rb_node = RBTreeNode(9)
        rb_node_right = RBTreeNode(10)
        sol = Solution()
        sol.RBInsert(rb_tree, rb_node)
        sol.RBInsert(rb_tree, rb_node_right)
        self.assertEqual(rb_tree.root.right.key, rb_node_right.key)

    # вставка узла дерева
    def test_tree_insert(self):
        rb_tree = RBTree()
        rb_node = RBTreeNode(9)
        rb_node_left = RBTreeNode(4)
        rb_node_right = RBTreeNode(20)
        sol = Solution()
        sol.RBInsert(rb_tree, rb_node)
        sol.RBInsert(rb_tree, rb_node_left)
        sol.RBInsert(rb_tree, rb_node_right)

        rb_node_insert = RBTreeNode(3)
        sol.RBInsert(rb_tree, rb_node_insert)
        self.assertEqual(rb_tree.root.left.left.key, rb_node_insert.key)
        self.assertEqual(rb_tree.root.left.left.color, 'red')

        rb_node_insert = RBTreeNode(5)
        sol.RBInsert(rb_tree, rb_node_insert)
        self.assertEqual(rb_tree.root.left.right.key, rb_node_insert.key)
        self.assertEqual(rb_tree.root.left.right.color, 'red')

    # удаление корня дерева
    def test_tree_delete_root(self):
        rb_tree = RBTree()
        sol = Solution()
        rb_node_insert = RBTreeNode(9)
        sol.RBInsert(rb_tree, rb_node_insert)
        rb_node_insert = RBTreeNode(4)
        sol.RBInsert(rb_tree, rb_node_insert)
        rb_node_insert = RBTreeNode(20)
        sol.RBInsert(rb_tree, rb_node_insert)
        rb_node_insert = RBTreeNode(3)
        sol.RBInsert(rb_tree, rb_node_insert)
        rb_node_insert = RBTreeNode(5)
        sol.RBInsert(rb_tree, rb_node_insert)

        sol.RBDelete(rb_tree, rb_tree.root)

        self.assertEqual(rb_tree.root.key, 4)
        self.assertEqual(rb_tree.root.color, 'black')
        self.assertEqual(rb_tree.root.left.key, 3)
        self.assertEqual(rb_tree.root.left.color, 'black')
        self.assertEqual(rb_tree.root.right.key, 20)
        self.assertEqual(rb_tree.root.right.color, 'black')
        self.assertEqual(rb_tree.root.right.left.key, 5)
        self.assertEqual(rb_tree.root.right.left.color, 'red')


if __name__ == '__main__':
    unittest.main()
