# delete node in a bst
# https://neetcode.io/problems/delete-node-in-a-bst/question
# code by aveia@github

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root, key: int):

        def insert_at_right_end(root, node):
            if not root:
                return node

            root.right = insert_at_right_end(root.right, node)
            return root

        def delete(root):
            if not root:
                return root

            if key == root.val:
                if root.left is None or root.right is None:
                    return root.left or root.right

                left = insert_at_right_end(root.left, root.right.left)
                root = root.right
                root.left = left

            elif key < root.val:
                root.left = delete(root.left)

            else:
                root.right = delete(root.right)

            return root

        return delete(root)
