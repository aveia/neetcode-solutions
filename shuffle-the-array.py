# shuffle the array
# https://neetcode.io/problems/shuffle-the-array/question
# code by aveia@github

class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        '''O(n ^ 2) time, O(1) space'''
        for i in range(n, 2 * n):
            for j in range(2 * n - i - 1):
                nums[i - j], nums[i - j - 1] = nums[i - j - 1], nums[i - j]
        return nums
