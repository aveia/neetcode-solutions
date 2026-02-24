# find minimum in rotated sorted array
# https://neetcode.io/problems/find-minimum-in-rotated-sorted-array/question
# code by aveia@github

class Solution:
    def findMin(self, ns: list[int]) -> int:
        n = len(ns)
        i, j = (0, n - 1)
        while i < j:
            m = (i + j) // 2
            if ns[m] == max(ns[i], ns[m], ns[j]):
                i = m + 1
            else:
                j = m
        return ns[i]
