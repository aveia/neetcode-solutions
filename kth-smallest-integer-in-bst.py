# kth smallest integer in bst
# https://neetcode.io/problems/kth-smallest-integer-in-bst/question
# code by aveia@github

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root, k: int) -> int:

        # returns either (True, solution) or (False, node count)
        def count(root, k):

            if not root:
                return False, 0

            found, left = count(root.left, k)
            if found:
                return True, left

            k -= left
            if k == 1:
                return True, root.val

            k -= 1

            found, right = count(root.right, k)
            if found:
                return True, right

            return False, left + 1 + right

        _, kth_smallest = count(root, k)

        return kth_smallest
