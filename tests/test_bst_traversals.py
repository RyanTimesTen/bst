import unittest

from bst import Node
from .test_bst_base import TestBSTBase

class TestBSTLevelOrderTraversal(TestBSTBase):
    def test_null(self):
        result = self.subject.traverse(mode='level_order')

        self.assertIsNone(result)

    def test_root(self):
        self.subject.root = Node(100)

        result = self.subject.traverse(mode='level_order')

        self.assertEqual([100], result)

    def test_left(self):
        self.subject.root = Node(80)
        self.subject.root.left = Node(30)

        result = self.subject.traverse(mode='level_order')

        self.assertEqual([80, 30], result)

    def test_right(self):
        self.subject.root = Node(80)
        self.subject.root.right = Node(100)

        result = self.subject.traverse(mode='level_order')

        self.assertEqual([80, 100], result)

    def test_left_subtree(self):
        self.subject.root = Node(5)
        self.subject.root.left = Node(4)
        self.subject.root.left.left = Node(3)

        result = self.subject.traverse(mode='level_order')

        self.assertEqual([5, 4, 3], result)

    def test_right_subtree(self):
        self.subject.root = Node(3)
        self.subject.root.right = Node(4)
        self.subject.root.right.right = Node(5)

        result = self.subject.traverse(mode='level_order')

        self.assertEqual([3, 4, 5], result)

    def test_uneven_tree(self):
        self.subject.root = Node(10)
        self.subject.root.left = Node(8)
        self.subject.root.right = Node(12)
        self.subject.root.left.right = Node(9)
        self.subject.root.right.left = Node(11)

        result = self.subject.traverse(mode='level_order')

        self.assertEqual([10, 8, 12, 9, 11], result)

    def test_full_tree(self):
        self.setup_full_tree()

        result = self.subject.traverse(mode='level_order')

        self.assertEqual([25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90], result)

    def test_medium_tree(self):
        for i in range(-400, 400):
            self.subject.insert(i)

        result = self.subject.traverse(mode='level_order')

        self.assertEqual(len(result), 800)

    @unittest.skip('This test case causes maximum recursion depth error.')
    def test_large_tree(self):
        for i in range(-100_000_000, 100_000_000):
            self.subject.insert(i)

        result = self.subject.traverse(mode='level_order')

        self.assertEqual(len(result), 200_00_000)

class TestBSTInorderTraversal(TestBSTBase):
    def test_null(self):
        result = self.subject.traverse(mode='inorder')

        self.assertIsNone(result)

    def test_root(self):
        self.subject.root = Node(100)

        result = self.subject.traverse(mode='inorder')

        self.assertEqual([100], result)

    def test_left(self):
        self.subject.root = Node(80)
        self.subject.root.left = Node(30)

        result = self.subject.traverse(mode='inorder')

        self.assertEqual([30, 80], result)

    def test_right(self):
        self.subject.root = Node(80)
        self.subject.root.right = Node(100)

        result = self.subject.traverse(mode='inorder')

        self.assertEqual([80, 100], result)

    def test_left_subtree(self):
        self.subject.root = Node(5)
        self.subject.root.left = Node(4)
        self.subject.root.left.left = Node(3)

        result = self.subject.traverse(mode='inorder')

        self.assertEqual([3, 4, 5], result)

    def test_right_subtree(self):
        self.subject.root = Node(3)
        self.subject.root.right = Node(4)
        self.subject.root.right.right = Node(5)

        result = self.subject.traverse(mode='inorder')

        self.assertEqual([3, 4, 5], result)

    def test_uneven_tree(self):
        self.subject.root = Node(10)
        self.subject.root.left = Node(8)
        self.subject.root.right = Node(12)
        self.subject.root.left.right = Node(9)
        self.subject.root.right.left = Node(11)

        result = self.subject.traverse(mode='inorder')

        self.assertEqual([8, 9, 10, 11, 12], result)

    def test_full_tree(self):
        self.setup_full_tree()

        result = self.subject.traverse(mode='inorder')

        self.assertEqual([4, 10, 12, 15, 18, 22, 24, 25, 31, 35, 44, 50, 66, 70, 90], result)

    def test_medium_tree(self):
        for i in range(-400, 400):
            self.subject.insert(i)

        result = self.subject.traverse(mode='inorder')

        self.assertEqual(len(result), 800)

    @unittest.skip('This test case causes maximum recursion depth error.')
    def test_large_tree(self):
        for i in range(-100_000_000, 100_000_000):
            self.subject.insert(i)

        result = self.subject.traverse(mode='inorder')

        self.assertEqual(len(result), 200_00_000)

class TestBSTPreorderTraversal(TestBSTBase):
    def test_null(self):
        result = self.subject.traverse(mode='preorder')

        self.assertIsNone(result)

    def test_root(self):
        self.subject.root = Node(100)

        result = self.subject.traverse(mode='preorder')

        self.assertEqual([100], result)

    def test_left(self):
        self.subject.root = Node(80)
        self.subject.root.left = Node(30)

        result = self.subject.traverse(mode='preorder')

        self.assertEqual([80, 30], result)

    def test_right(self):
        self.subject.root = Node(80)
        self.subject.root.right = Node(100)

        result = self.subject.traverse(mode='preorder')

        self.assertEqual([80, 100], result)

    def test_left_subtree(self):
        self.subject.root = Node(5)
        self.subject.root.left = Node(4)
        self.subject.root.left.left = Node(3)

        result = self.subject.traverse(mode='preorder')

        self.assertEqual([5, 4, 3], result)

    def test_right_subtree(self):
        self.subject.root = Node(3)
        self.subject.root.right = Node(4)
        self.subject.root.right.right = Node(5)

        result = self.subject.traverse(mode='preorder')

        self.assertEqual([3, 4, 5], result)

    def test_uneven_tree(self):
        self.subject.root = Node(10)
        self.subject.root.left = Node(8)
        self.subject.root.right = Node(12)
        self.subject.root.left.right = Node(9)
        self.subject.root.right.left = Node(11)

        result = self.subject.traverse(mode='preorder')

        self.assertEqual([10, 8, 9, 12, 11], result)

    def test_full_tree(self):
        self.setup_full_tree()

        result = self.subject.traverse(mode='preorder')

        self.assertEqual([25, 15, 10, 4, 12, 22, 18, 24, 50, 35, 31, 44, 70, 66, 90], result)

    def test_medium_tree(self):
        for i in range(-400, 400):
            self.subject.insert(i)

        result = self.subject.traverse(mode='preorder')

        self.assertEqual(len(result), 800)

    @unittest.skip('This test case causes maximum recursion depth error.')
    def test_large_tree(self):
        for i in range(-100_000_000, 100_000_000):
            self.subject.insert(i)

        result = self.subject.traverse(mode='preorder')

        self.assertEqual(len(result), 200_00_000)

class TestBSTPostorderTraversal(TestBSTBase):
    def test_null(self):
        result = self.subject.traverse(mode='postorder')

        self.assertIsNone(result)

    def test_root(self):
        self.subject.root = Node(100)

        result = self.subject.traverse(mode='postorder')

        self.assertEqual([100], result)

    def test_left(self):
        self.subject.root = Node(80)
        self.subject.root.left = Node(30)

        result = self.subject.traverse(mode='postorder')

        self.assertEqual([30, 80], result)

    def test_right(self):
        self.subject.root = Node(80)
        self.subject.root.right = Node(100)

        result = self.subject.traverse(mode='postorder')

        self.assertEqual([100, 80], result)

    def test_left_subtree(self):
        self.subject.root = Node(5)
        self.subject.root.left = Node(4)
        self.subject.root.left.left = Node(3)

        result = self.subject.traverse(mode='postorder')

        self.assertEqual([3, 4, 5], result)

    def test_right_subtree(self):
        self.subject.root = Node(3)
        self.subject.root.right = Node(4)
        self.subject.root.right.right = Node(5)

        result = self.subject.traverse(mode='postorder')

        self.assertEqual([5, 4, 3], result)

    def test_uneven_tree(self):
        self.subject.root = Node(10)
        self.subject.root.left = Node(8)
        self.subject.root.right = Node(12)
        self.subject.root.left.right = Node(9)
        self.subject.root.right.left = Node(11)

        result = self.subject.traverse(mode='postorder')

        self.assertEqual([9, 8, 11, 12, 10], result)

    def test_full_tree(self):
        self.setup_full_tree()

        result = self.subject.traverse(mode='postorder')

        self.assertEqual([4, 12, 10, 18, 24, 22, 15, 31, 44, 35, 66, 90, 70, 50, 25], result)

    def test_medium_tree(self):
        for i in range(-400, 400):
            self.subject.insert(i)

        result = self.subject.traverse(mode='postorder')

        self.assertEqual(len(result), 800)

    @unittest.skip('This test case causes maximum recursion depth error.')
    def test_large_tree(self):
        for i in range(-100_000_000, 100_000_000):
            self.subject.insert(i)

        result = self.subject.traverse(mode='postorder')

        self.assertEqual(len(result), 200_00_000)

if __name__ == '__main__':
    unittest.main()
