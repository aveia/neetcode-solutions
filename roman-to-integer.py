# roman to integer
# https://neetcode.io/problems/roman-to-integer/question
# code by aveia@github

class Solution:
    def romanToInt(self, s: str) -> int:
        r2d = {
            'I': 1,   'V': 5,
            'X': 10,  'L': 50,
            'C': 100, 'D': 500,
            'M': 1000,
        }
        i, v = 0, 0
        while i < len(s):
            if i + 1 < len(s) and r2d[s[i]] < r2d[s[i + 1]]:
                v += r2d[s[i + 1]] - r2d[s[i]]
                i += 2
            else:
                v += r2d[s[i]]
                i += 1
        return v
