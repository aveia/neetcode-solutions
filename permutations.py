# permutations
# https://neetcode.io/problems/permutations/question
# code by aveia@github

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        def perms(ns):
            if len(ns) == 1:
                return [ns]
            ps = []
            for i in range(len(ns)):
                for perm in perms(ns[:i] + ns[i + 1:]):
                    ps.append([ns[i]] + perm)
            return ps

        return perms(nums)
