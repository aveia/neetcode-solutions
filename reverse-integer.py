# reverse integer
# https://neetcode.io/problems/reverse-integer/question
# code by aveia@github

class Solution:
    def reverse(self, x: int) -> int:

        if not x:
            return 0

        sign = x // abs(x)
        x *= sign
        s = str(x)

        max_s = str(2 ** 31 if sign < 0 else 2 ** 31 - 1)
        s0 = '0' * (len(max_s) - len(s)) + ''.join(reversed(s))
        if s0 > max_s:
            return 0

        return sign * int(''.join(reversed(s)))
