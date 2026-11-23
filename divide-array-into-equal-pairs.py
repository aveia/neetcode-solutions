# divide array into equal pairs
# https://neetcode.io/problems/divide-array-into-equal-pairs/question
# code by aveia@github

class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        from collections import defaultdict

        hist = defaultdict(int)
        for n in nums:
            hist[n] += 1

        for k in hist:
            if hist[k] % 2:
                return False
        return True
