# kth largest element in an array
# https://neetcode.io/problems/kth-largest-element-in-an-array/question
# code by aveia@github

# TODO: never let the heap contain more than k items

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        import heapq as hq

        hq.heapify(nums)
        for _ in range(len(nums) - k):
            hq.heappop(nums)

        return hq.heappop(nums)
