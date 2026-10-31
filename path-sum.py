# path sum
# https://neetcode.io/problems/path-sum/question
# code by aveia@github

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:

        def path(root, prev=0):
            if not root:
                return False
            if not (root.left or root.right):
                return prev + root.val == targetSum
            return path(root.left, prev + root.val) or path(root.right, prev + root.val)

        return path(root)
