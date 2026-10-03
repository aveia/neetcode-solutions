# search insert position
# https://neetcode.io/problems/search-insert-position/question
# code by aveia@github

# TODO: explain both versions

class Solution:

    # def searchInsert(self, nums: list[int], target: int) -> int:
    #     i, j = 0, len(nums) - 1
    #     m = (i + j) // 2
    #     while i <= j:
    #         k = nums[m]
    #         if target > k:
    #             i = m + 1
    #         elif target < k:
    #             j = m - 1
    #         else:
    #             return m
    #         m = (i + j) // 2
    #     return m + 1

    def searchInsert(self, nums: list[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            k = nums[m]
            if target > k:
                i = m + 1
            elif target < k:
                j = m - 1
            else:
                return m
        return i
