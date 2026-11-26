# path with minimum effort
# https://neetcode.io/problems/path-with-minimum-effort/question
# code by aveia@github

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        import heapq as hq

        n, m = len(heights), len(heights[0])
        heap = [(0, 0, 0)]
        seen = set()

        while heap:
            max_effort, i, j = hq.heappop(heap)

            if (i, j) == (n - 1, m - 1):
                return max_effort

            if (i, j) in seen:
                continue

            seen.add((i, j))

            for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if not (0 <= a < n and 0 <= b < m) or (a, b) in seen:
                    continue

                effort = max(max_effort, abs(heights[a][b] - heights[i][j]))
                hq.heappush(heap, (effort, a, b))

        return 0
