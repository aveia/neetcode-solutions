# serialize and deserialize binary tree
# https://neetcode.io/problems/serialize-and-deserialize-binary-tree/question
# code by aveia@github

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        def encode(r):
            if not r:
                return '#'
            return f'{r.val}[{encode(r.left)},{encode(r.right)}]'

        return encode(root)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        def decode(i):
            if data[i] == '#':
                return None, i + 1
            val = ''
            while data[i] in '0123456789':
                val += data[i]
                i += 1
            val = int(val)
            i += 1 # skip '['
            left, i = decode(i)
            i += 1 # skip ','
            right, i = decode(i)
            return TreeNode(val, left, right), i + 1 # skip ']'

        return decode(0)[0]
