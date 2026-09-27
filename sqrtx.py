# sqrt(x)
# https://neetcode.io/problems/sqrtx/question
# code by aveia@github

class Solution:

    # def mySqrt(self, x: int) -> int:
    #     k = x
    #     for i in range(2, x):
    #         k = x // i
    #         if k * k <= x:
    #             break
    #     while k * k <= x:
    #         k += 1
    #     return k - 1

    def mySqrt(self, x: int) -> int:
        i, j = 0, x
        while abs(i - j) > 1:
            m = (i + j) // 2
            if m * m > x:
                j = m - 1
            elif m * m <= x:
                i = m
        while i * i <= x:
            i += 1
        return i - 1

