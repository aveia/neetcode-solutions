# valid binary search tree
# https://neetcode.io/problems/valid-binary-search-tree/question
# code by aveia@github

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root) -> bool:

        def is_valid(root):

            if not root:
                return True, None, None

            if not root.left and not root.right:
                return True, root.val, root.val

            valid, min_left, max_left = is_valid(root.left)
            if not valid or max_left is not None and max_left >= root.val:
                return False, None, None
            min_root = root.val if min_left is None else min(min_left, root.val)

            valid, min_right, max_right = is_valid(root.right)
            if not valid or min_right is not None and min_right <= root.val:
                return False, None, None
            max_root = root.val if max_right is None else max(max_right, root.val)

            return True, min_root, max_root

        valid, _, _ = is_valid(root)
        return valid
