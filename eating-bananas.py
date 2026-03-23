# koko eating bananas
# https://neetcode.io/problems/eating-bananas/question
# code by aveia@github

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        def satisfies(k):
            hours = 0
            for x in piles:
                hours += math.ceil(x / k)
            return hours <= h

        import math
        min_k = math.ceil(sum(piles) / h)
        max_k = max(piles[0], *piles) # fixes the `len(piles) == 1` case

        while min_k < max_k:
            mid_k = (min_k + max_k) // 2
            if satisfies(mid_k):
                max_k = mid_k
            else:
                min_k = mid_k + 1

        return min_k
