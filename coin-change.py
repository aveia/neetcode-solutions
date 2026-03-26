# coin change
# https://neetcode.io/problems/coin-change/question
# code by aveia@github

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        qty_coins = [-1] * (amount + 1)
        qty_coins[0] = 0

        for am in range(1, amount + 1):

            if am in coins:
                qty_coins[am] = 1
                continue

            min_coins = -1
            for coin in coins:
                if am - coin < 0:
                    continue
                rem = qty_coins[am - coin]
                if rem == -1:
                    continue
                c = rem + 1
                min_coins = c if min_coins == -1 else min(min_coins, c)

            qty_coins[am] = min_coins

        return qty_coins[amount]
