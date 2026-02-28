# longest palindromic substring
# https://neetcode.io/problems/longest-palindromic-substring/question
# code by aveia@github

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        n = len(s)

        from collections import defaultdict
        m = defaultdict(list)

        for i in range(1, n):
            m[0].append((i, i - 1))
        for i in range(n):
            m[1].append((i, i))

        for size in range(2, n + 1):
            for (a, b) in m[size - 2]:
                if a - 1 < 0 or b + 1 >= n:
                    continue
                if s[a - 1] == s[b + 1]:
                    m[size].append((a - 1, b + 1))

        for size in range(n, 0, -1):
            if m[size]:
                a, b = m[size][0]
                return s[a : b+1]

        return ""
