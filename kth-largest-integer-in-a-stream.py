# kth largest element in a stream
# https://neetcode.io/problems/kth-largest-integer-in-a-stream/question
# code by aveia@github

import heapq as hq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        hq.heapify(nums)
        self.nums = nums
        self.k = k
        while len(nums) > k:
            hq.heappop(self.nums)

    def add(self, val: int) -> int:
        hq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            hq.heappop(self.nums)
        if len(self.nums) == self.k:
            return self.nums[0]
        return None
