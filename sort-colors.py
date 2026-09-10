# sort colors
# https://neetcode.io/problems/sort-colors/question
# code by aveia@github

# TODO: one-pass algorithm

class Solution:
    def sortColors(self, nums: list[int]) -> None:

        qty = [0, 0, 0]
        for n in nums:
            qty[n] += 1

        i = 0
        for n in range(3):
            for _ in range(qty[n]):
                nums[i] = n
                i += 1
