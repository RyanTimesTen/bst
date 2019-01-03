import unittest

from bst import BST, Node

class TestBSTBase(unittest.TestCase):
    def setUp(self):
        self.subject = BST()

class TestBSTInsert(TestBSTBase):
    def test_null(self):
        result = self.subject.insert(100)

        self.assertIsNotNone(self.subject.root)
        self.assertEqual(self.subject.root, result)

    def test_duplicate_at_root(self):
        self.subject.insert(100)

        result = self.subject.insert(100)

        self.assertIsNone(result)

    def test_duplicate(self):
        self.subject.insert(100)
        self.subject.insert(200)

        result = self.subject.insert(200)

        self.assertIsNone(result)

    def test_left(self):
        self.subject.insert(100)

        result = self.subject.insert(99)

        self.assertIsNotNone(self.subject.root.left)
        self.assertEqual(self.subject.root.left, result)
    
    def test_right(self):
        self.subject.insert(100)

        result = self.subject.insert(101)

        self.assertIsNotNone(self.subject.root.right)
        self.assertEqual(self.subject.root.right, result)

    def test_left_subtree(self):
        self.subject.insert(100)
        self.subject.insert(90)

        result = self.subject.insert(80)

        left_subtree = self.subject.root.left
        self.assertIsNotNone(left_subtree.left)
        self.assertEqual(left_subtree.left, result)

    def test_right_subtree(self):
        self.subject.insert(100)
        self.subject.insert(110)

        result = self.subject.insert(120)

        right_subtree = self.subject.root.right
        self.assertIsNotNone(right_subtree.right)
        self.assertEqual(right_subtree.right, result)

class TestBSTSearch(TestBSTBase):
    def test_null(self):
        result = self.subject.search(100)

        self.assertIsNone(result)

    def test_root(self):
        self.subject.root = Node(100)

        result = self.subject.search(100)

        self.assertEqual(Node(100), result)

    def test_left(self):
        self.subject.root = Node(100)
        self.subject.root.left = Node(50)

        result = self.subject.search(50)

        self.assertEqual(Node(50), result)

    def test_right(self):
        self.subject.root = Node(100)
        self.subject.root.right = Node(150)

        result = self.subject.search(150)

        self.assertEqual(Node(150), result)
    
    def test_left_subtree(self):
        self.subject.root = Node(100)
        self.subject.root.left = Node(75)
        self.subject.root.left.left = Node(50)

        result = self.subject.search(50)

        self.assertEqual(Node(50), result)

    def test_right_subtree(self):
        self.subject.root = Node(100)
        self.subject.root.right = Node(125)
        self.subject.root.right.right = Node(150)

        result = self.subject.search(150)

        self.assertEqual(Node(150), result)

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

if __name__ == '__main__':
    unittest.main()
