# contains duplicate
# https://neetcode.io/problems/duplicate-integer/question
# code by aveia@github

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False
