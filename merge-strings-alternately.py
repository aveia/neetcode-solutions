# merge strings alternately
# https://neetcode.io/problems/merge-strings-alternately/question
# code by aveia@github

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = min(len(word1), len(word2))
        res = ''
        for i in range(m):
            res += word1[i]
            res += word2[i]
        res += word1[m:]
        res += word2[m:]
        return res
