# palindromic substrings
# https://neetcode.io/problems/palindromic-substrings/question
# code by aveia@github

class Solution:
    def countSubstrings(self, s: str) -> int:

        if not s:
            return 0
        elif len(s) == 1:
            return 1

        n = len(s)

        from collections import defaultdict
        m = defaultdict(list)

        for i in range(n):
            m[1].append((i, i))
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                m[2].append((i, i + 1))

        qty = len(m[1]) + len(m[2])
        for size in range(3, n + 1):
            for (a, b) in m[size - 2]:
                if a - 1 < 0 or b + 1 >= n:
                    continue
                if s[a - 1] == s[b + 1]:
                    m[size].append((a - 1, b + 1))
            qty += len(m[size])
            del m[size - 2]

        return qty
