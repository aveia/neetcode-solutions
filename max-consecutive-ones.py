# max consecutive ones
# https://neetcode.io/problems/max-consecutive-ones/question
# code by aveia@github

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        mx, qty = 0, 0
        for n in nums:
            if n:
                qty += 1
            else:
                qty = 0
            mx = max(mx, qty)
        return mx
