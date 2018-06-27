import unittest


def is_binary_search_tree(root):
    # Determine if the tree is a valid binary search tree
    # Arbitrary.

    if not root.left and not root.right:
        return True

    if not root.right:
        return isBST(root.left, root.value, True)

    if not root.left:
        return isBST(root.right, root.value, False)

    return isBST(root.left, root.value, True) and isBST(root.right, root.value, False)

def isBST(root, target, going_left=False):
    if (not root.left) or (not root.right):
        if root.left:
            return root.left.value < root.value and \
                   isBST(root.left, root.value, True)
        if root.right:
            return root.right.value > root.value and \
                   isBST(root.right, root.value, False)
        return True

    this_value = root.value
    left_value = root.left.value
    right_value = root.right.value

    if not (this_value > left_value) and (this_value < right_value):
        return False

    if going_left and not right_value < target:
        return False

    if not going_left and not left_value > target:
        return False

    return isBST(root.left, root.value, True) and isBST(root.right, root.value, False)

# Tests

class Test(unittest.TestCase):
    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

    def test_valid_full_tree(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_both_subtrees_valid(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(80)
        left.insert_left(20)
        left.insert_right(60)
        right.insert_left(70)
        right.insert_right(90)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_descending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(40)
        left_left = left.insert_left(30)
        left_left_left = left_left.insert_left(20)
        left_left_left.insert_left(10)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_out_of_order_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        right = tree.insert_right(70)
        right_right = right.insert_right(60)
        right_right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_one_node_tree(self):
        tree = Test.BinaryTreeNode(50)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)


unittest.main(verbosity=2)