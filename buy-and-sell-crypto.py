# best time to buy and sell stock
# https://neetcode.io/problems/buy-and-sell-crypto/question
# code by aveia@github

class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        ps = []
        for i in range(1, len(prices)):
            ps.append(prices[i] - prices[i - 1])

        m = 0
        cur = 0
        for p in ps:
            cur += p
            if cur < 0:
                cur = 0
            m = max(m, cur)
        return m
