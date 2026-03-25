# min cost to connect points
# https://neetcode.io/problems/min-cost-to-connect-points/question
# code by aveia@github

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:

        from collections import defaultdict
        edges = []
        node2component = {}
        component2nodes = defaultdict(list)

        for i, (x0, y0) in enumerate(points):
            node2component[i] = i
            component2nodes[i].append(i)
            for j in range(i + 1, len(points)):
                x1, y1 = points[j]
                edges.append((abs(x1 - x0) + abs(y1 - y0), i, j))

        edges.sort()

        min_cost = 0
        for cost, i, j in edges:
            i_component = node2component[i]
            j_component = node2component[j]
            if i_component == j_component:
                continue
            min_cost += cost
            for k in component2nodes[j_component]:
                node2component[k] = i_component
                component2nodes[i_component].append(k)
            del component2nodes[j_component]
            if len(component2nodes) == 1:
                break
        return min_cost
