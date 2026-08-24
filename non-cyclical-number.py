# non-cyclical number
# https://neetcode.io/problems/non-cyclical-number/question
# code by aveia@github

class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, sum([int(x)**2 for x in str(n)])
        while slow != fast:
            slow = sum([int(x)**2 for x in str(slow)])
            fast = sum([int(x)**2 for x in str(fast)])
            fast = sum([int(x)**2 for x in str(fast)])
        return fast == 1
