# count odd numbers in an interval range
# https://neetcode.io/problems/count-odd-numbers-in-an-interval-range/question
# code by aveia@github

class Solution:
    # def countOdds(self, low: int, high: int) -> int:
    #     return (high - low + 1) // 2 + low % 2 * high % 2 # safe

    # def countOdds(self, low: int, high: int) -> int:
    #     return (high - low + 1 + low % 2 + high % 2) // 2 # safe and fun

    def countOdds(self, low: int, high: int) -> int:
        return (high - low + 1) // 2 + low * high % 2 # might overflow
