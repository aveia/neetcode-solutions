# sign of the product of an array
# https://neetcode.io/problems/sign-of-the-product-of-an-array/question
# code by aveia@github

class Solution:
    def arraySign(self, nums: list[int]) -> int:

        def signFunc(x):
            return 0 if not x else x // abs(x)

        p = 1
        for x in nums:
            p *= x

        return signFunc(p)
