# find k closest elements
# https://neetcode.io/problems/find-k-closest-elements/question
# code by aveia@github

class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        import heapq as hq

        heap = []
        for a in arr:
            hq.heappush(heap, (abs(a - x), a))

        res = []
        for _ in range(k):
            _, val = hq.heappop(heap)
            res.append(val)

        return sorted(res)
