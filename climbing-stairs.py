# climbing stairs
# https://neetcode.io/problems/climbing-stairs/question
# code by aveia@github

class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        prevprev = 1
        prev = 2
        for _ in range(3, n):
            prev = prev + prevprev
            prevprev = prev - prevprev

        return prev + prevprev
