# clone graph
# https://neetcode.io/problems/clone-graph/question
# code by aveia@github

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        new_nodes = {}
        def get_node(val):
            if val in new_nodes:
                return new_nodes[val]
            new_node = Node(val)
            new_nodes[val] = new_node
            return new_node

        stack = [node]
        visited = set()
        while stack:
            cur = stack.pop()
            if cur.val in visited:
                continue
            new_cur = get_node(cur.val)
            for neighbor in cur.neighbors:
                new_neighbor = get_node(neighbor.val)
                new_cur.neighbors.append(new_neighbor)
                stack.append(neighbor)
            visited.add(cur.val)

        return new_nodes[node.val]
