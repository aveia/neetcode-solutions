# binary tree level order traversal
# https://neetcode.io/problems/level-order-traversal-of-binary-tree/question
# code by aveia@github

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        from collections import deque

        levels = []
        cur_level = 0
        cur_level_list = []

        queue = deque()
        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            if node is None:
                continue
            if level != cur_level:
                levels.append(cur_level_list)
                cur_level = level
                cur_level_list = []
            cur_level_list.append(node.val)
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

        if cur_level_list:
            levels.append(cur_level_list)

        return levels
