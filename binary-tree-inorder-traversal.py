# binary tree inorder traversal
# https://neetcode.io/problems/binary-tree-inorder-traversal/question
# code by aveia@github

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root) -> list[int]:

        def ordered(root):
            if not root:
                return []
            return ordered(root.left) + [root.val] + ordered(root.right)

        return ordered(root)
