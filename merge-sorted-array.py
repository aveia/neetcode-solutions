# merge sorted array
# https://neetcode.io/problems/merge-sorted-array/question
# code by aveia@github

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        for i in range(m):
            nums1[m + n - 1 - i] = nums1[m - 1 - i]

        i, j, k = n, 0, 0
        while i < m + n and j < n:
            if nums1[i] < nums2[j]:
                nums1[k] = nums1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1

        if j == n:
            while i < m + n:
                nums1[k] = nums1[i]
                i += 1
                k += 1

        if i == m + n:
            while j < n:
                nums1[k] = nums2[j]
                j += 1
                k += 1
