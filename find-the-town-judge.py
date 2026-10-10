# find the town judge
# https://neetcode.io/problems/find-the-town-judge/question
# code by aveia@github

class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:

        trusted_by = n * [0]
        trusts = n * [0]
        for a, b in trust:
            trusts[a - 1] += 1
            trusted_by[b - 1] += 1

        for k in range(n):
            if not trusts[k] and trusted_by[k] == n - 1:
                return k + 1
        return -1
