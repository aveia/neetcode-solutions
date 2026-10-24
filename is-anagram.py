# valid anagram
# https://neetcode.io/problems/is-anagram/question
# code by aveia@github

class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return sorted(s) == sorted(t)

    # def isAnagram(self, s: str, t: str) -> bool:
    #     from collections import defaultdict
    #     def hist(x):
    #         h = defaultdict(int)
    #         for c in x:
    #             h[c] += 1
    #         return h
    #     return hist(s) == hist(t)

    def isAnagram(self, s: str, t: str) -> bool:
        def hist(x):
            h = 26 * [0]
            for c in x:
                h[ord(c) - ord('a')] += 1
            return h
        return hist(s) == hist(t)
