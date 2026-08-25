# balanced binary tree
# https://neetcode.io/problems/balanced-binary-tree/question
# code by aveia@github

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height_and_balanced(root):
            if not root:
                return 0, True

            left, left_balanced = height_and_balanced(root.left)
            right, right_balanced = height_and_balanced(root.right)

            return 1 + max(left, right), left_balanced and right_balanced and abs(left - right) <= 1

        _, balanced = height_and_balanced(root)
        return balanced
