# contains duplicate ii
# https://neetcode.io/problems/contains-duplicate-ii/question
# code by aveia@github

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        from collections import defaultdict
        qty = defaultdict(int)

        for i in range(min(len(nums), k + 1)):
            qty[nums[i]] += 1
            if qty[nums[i]] >= 2:
                return True

        for i in range(len(nums) - k - 1):
            qty[nums[i]] -= 1
            if not qty[nums[i]]:
                del qty[nums[i]]
            qty[nums[i + k + 1]] += 1
            if qty[nums[i + k + 1]] >= 2:
                return True

        return False
