# number of connected components in an undirected graph
# https://neetcode.io/problems/count-connected-components/question
# code by aveia@github

class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        from collections import defaultdict
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        visited = set()

        def visit(src):
            stack = [src]
            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                visited.add(node)
                for adj in adj_list[node]:
                    stack.append(adj)

        qty = 0
        for node in range(n):
            if node not in visited:
                qty += 1
                visit(node)

        return qty
