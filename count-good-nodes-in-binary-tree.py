# count good nodes in binary tree
# https://neetcode.io/problems/count-good-nodes-in-binary-tree/question
# code by aveia@github

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root) -> int:

        def good(root, largest=None):

            if not root:
                return 0

            if largest is None:
                largest = root.val

            qty = 1 if largest <= root.val else 0
            largest = max(largest, root.val)

            return qty + good(root.left, largest) + good(root.right, largest)

        return good(root)
