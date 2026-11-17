# best time to buy and sell stock ii
# https://neetcode.io/problems/best-time-to-buy-and-sell-stock-ii/question
# code by aveia@github

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            max_profit += profit if profit > 0 else 0
        return max_profit
