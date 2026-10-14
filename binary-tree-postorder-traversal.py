# binary tree postorder traversal
# https://neetcode.io/problems/binary-tree-postorder-traversal/question
# code by aveia@github

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root) -> list[int]:

        def post(root):
            if not root:
                return []
            return post(root.left) + post(root.right) + [root.val]

        return post(root)
