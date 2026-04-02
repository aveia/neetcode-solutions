# diameter of binary tree
# https://neetcode.io/problems/binary-tree-diameter/question
# code by aveia@github

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root) -> int:

        diameter = 0

        def height(root):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return 0
            left_height = height(root.left) + 1 if root.left else 0
            right_height = height(root.right) + 1 if root.right else 0
            nonlocal diameter
            diameter = max(diameter, left_height + right_height)
            return max(left_height, right_height)

        height(root)
        return diameter
