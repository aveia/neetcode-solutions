# k closest points to origin
# https://neetcode.io/problems/k-closest-points-to-origin/question
# code by aveia@github

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        import heapq as hq

        heap = []
        for x, y in points:
            squared_distance = x*x + y*y
            hq.heappush(heap, (squared_distance, x, y))

        res = []
        for _ in range(k):
            _, x, y = hq.heappop(heap)
            res.append([x, y])

        return res
