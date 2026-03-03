# graph valid tree
# https://neetcode.io/problems/valid-tree/question
# code by aveia@github

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        from collections import defaultdict
        node2component = {}
        component2nodes = defaultdict(list)

        for i in range(n):
            node2component[i] = i
            component2nodes[i].append(i)

        for edge in edges:
            a, b = sorted(edge)
            component_a = node2component[a]
            component_b = node2component[b]
            if component_a == component_b:
                return False
            for c in component2nodes[component_b]:
                node2component[c] = component_a
                component2nodes[component_a].append(c)
            del component2nodes[component_b]

        return len(component2nodes) == 1
