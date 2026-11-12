# jump game
# https://neetcode.io/problems/jump-game/question
# code by aveia@github

# TODO: O(n) time, O(1) space

class Solution:
    def canJump(self, nums: list[int]) -> bool:

        n = len(nums)
        can_reach = [False] * n
        can_reach[-1] = True

        for i in range(n - 2, -1, -1):
            for j in range(min(nums[i], n - i - 1), 0, -1):
                if can_reach[i + j]:
                    can_reach[i] = True
                    break

        return can_reach[0]
