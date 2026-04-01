# redundant connection
# https://neetcode.io/problems/redundant-connection/question
# code by aveia@github

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        from collections import defaultdict

        node2component = {}
        component2nodes = defaultdict(list)

        for node in range(1, len(edges) + 1):
            node2component[node] = node
            component2nodes[node].append(node)

        for a, b in edges:

            if node2component[a] == node2component[b]:
                return [a, b]

            a, b = sorted([a, b])
            a_component = node2component[a]
            b_component = node2component[b]

            for node in component2nodes[b_component]:
                node2component[node] = a_component
                component2nodes[a_component].append(node)

            del component2nodes[b_component]
