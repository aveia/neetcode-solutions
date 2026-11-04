# coin change ii
# https://neetcode.io/problems/coin-change-ii/question
# code by aveia@github

class Solution:
    def change(self, amount: int, coins: list[int]) -> int:

        memo = {}

        def combinations(target, min_coin):
            if not target:
                return 1

            if (target, min_coin) in memo:
                return memo[(target, min_coin)]

            c = 0
            for coin in coins:
                if coin <= target and coin >= min_coin:
                    c += combinations(target - coin, coin)
            memo[target, min_coin] = c
            return c

        return combinations(amount, 1)
