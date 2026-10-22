# integer break
# https://neetcode.io/problems/integer-break/question
# code by aveia@github

# TODO: make it linear

class Solution:
    def integerBreak(self, n: int) -> int:

        mp = (n + 1) * [0]

        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                mp[i] = max(mp[i], max(mp[i - j], i - j) * max(mp[j], j))

        return mp[n]
