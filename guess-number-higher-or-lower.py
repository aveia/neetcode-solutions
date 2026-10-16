# guess number higher or lower
# https://neetcode.io/problems/guess-number-higher-or-lower/question
# code by aveia@github

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        i, j = 1, n
        g = (i + j) // 2
        while r := guess(g):
            if r < 0:
                j = g - 1
            else:
                i = g + 1
            g = (i + j) // 2
        return g
