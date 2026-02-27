# longest common subsequence
# https://neetcode.io/problems/longest-common-subsequence/question
# code by aveia@github

class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:

        lcs = [[0] * len(s2) for _ in range(len(s1))]
        def get(i, j):
            if i == -1 or j == -1:
                return 0
            return lcs[i][j]

        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    lcs[i][j] = get(i - 1, j - 1) + 1
                else:
                    lcs[i][j] = max(get(i - 1, j), get(i, j - 1))

        return lcs[len(s1) - 1][len(s2) - 1]
