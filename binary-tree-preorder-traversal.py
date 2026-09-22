# binary tree preorder traversal
# https://neetcode.io/problems/binary-tree-preorder-traversal/question
# code by aveia@github

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root) -> list[int]:

        def pre(root):
            if not root:
                return []
            return [root.val] + pre(root.left) + pre(root.right)

        return pre(root)
