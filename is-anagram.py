# valid anagram
# https://neetcode.io/problems/is-anagram/question
# code by aveia@github

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
