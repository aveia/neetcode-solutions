# stone game
# https://neetcode.io/problems/stone-game/question
# code by aveia@github

class Solution:
    # def stoneGame(self, piles: list[int]) -> bool:
    #     return True # guess what, alice always wins

    def stoneGame(self, piles: list[int]) -> bool:
        n = len(piles)
        memo = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n): # bob always takes the last stone
            memo[i][i] = -1 * piles[i]

        def score_diff(i, j):
            if memo[i][j] is not None:
                return memo[i][j]

            is_bob = (j - i + 1) % 2
            sign = -1 if is_bob else 1

            take_left = sign * piles[i] + score_diff(i + 1, j)
            take_right = sign * piles[j] + score_diff(i, j - 1)

            if is_bob:
                memo[i][j] = min(take_left, take_right)
            else:
                memo[i][j] = max(take_left, take_right)
            return memo[i][j]

        return score_diff(0, n - 1) > 0
