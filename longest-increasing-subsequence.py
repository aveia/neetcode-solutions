# longest increasing subsequence
# https://neetcode.io/problems/longest-increasing-subsequence/question
# code by aveia@github

# TODO: improve it

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        lis = n * [1]
        longest = bool(n) * 1

        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], lis[j] + 1)
                    if lis[i] > longest:
                        longest = lis[i]

        return longest
