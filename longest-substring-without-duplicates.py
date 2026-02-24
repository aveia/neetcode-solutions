# longest substring without repeating characters
# https://neetcode.io/problems/longest-substring-without-duplicates/question
# code by aveia@github

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        from collections import defaultdict
        i, j = 0, 0
        max_s = 0
        hist = defaultdict(int)
        while i < len(s) and j < len(s):
            hist[s[j]] += 1
            while hist[s[j]] > 1:
                hist[s[i]] -= 1
                i += 1
            max_s = max(j - i + 1, max_s)
            j += 1
        return max_s
