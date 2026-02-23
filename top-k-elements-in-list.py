# top k frequent elements
# https://neetcode.io/problems/top-k-elements-in-list/question
# code by aveia@github

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import defaultdict
        hist = defaultdict(int)
        for n in nums:
            hist[n] += 1
        return [v for c, v in sorted((-c, n) for (n, c) in hist.items())[:k]]
