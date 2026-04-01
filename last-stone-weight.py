# last stone weight
# https://neetcode.io/problems/last-stone-weight/question
# code by aveia@github

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        import heapq as hq
        hq.heapify_max(stones)
        while len(stones) > 1:
            big, small = hq.heappop_max(stones), hq.heappop_max(stones)
            if big == small:
                continue
            hq.heappush_max(stones, big - small)
        return stones.pop() if stones else 0
