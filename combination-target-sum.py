# combination sum
# https://neetcode.io/problems/combination-target-sum/question
# code by aveia@github

class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums = sorted(nums)

        def combinations(nums, target):
            if target == 0:
                return [[]]
            all_combinations = []
            for i, num in enumerate(nums):
                if num > target:
                    break
                cs = combinations(nums[i:], target - num)
                for c in cs:
                    all_combinations.append([num] + c)
            return all_combinations

        return combinations(nums, target)
