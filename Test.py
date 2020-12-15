import unittest
from RBTree import RBTreeNode


class RbTreeTests(unittest.TestCase):

    # инициализация узла дерева
    def test_node_init(self):
        nil = RBTreeNode(15)
        self.assertEqual(nil.key, 15)
        self.assertIsNone(nil.left, None)
        self.assertIsNone(nil.right, None)
        self.assertIsNone(nil.parent, None)
        self.assertEqual(nil.color, 'black')


if __name__ == '__main__':
    unittest.main()