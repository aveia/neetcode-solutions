# search in rotated sorted array
# https://neetcode.io/problems/find-target-in-rotated-sorted-array/question
# code by aveia@github

class Solution:
    def search(self, ns: list[int], target: int) -> int:
        n = len(ns)
        i, j = (0, n - 1)
        while i <= j:
            m = (i + j) // 2
            if target == ns[m]:
                return m
            elif target < ns[m]:
                if target >= ns[i] or ns[m] < ns[j]:
                    j = m - 1
                else:
                    i = m + 1
            else:
                if target <= ns[j] or ns[m] > ns[i]:
                    i = m + 1
                else:
                    j = m - 1
        return -1
