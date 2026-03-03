# lowest common ancestor in binary search tree
# https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree/question
# code by aveia@github

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None
        if p.val == root.val or q.val == root.val:
            return root
        if p.val < root.val and q.val > root.val or p.val > root.val and q.val < root.val:
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
