# products of array except self
# https://neetcode.io/problems/products-of-array-discluding-self/question
# code by aveia@github

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        p = 1
        n_zeros = 0
        for n in nums:
            if n == 0:
                n_zeros += 1
            else:
                p *= n
        out = []
        for n in nums:
            if n_zeros > 1:
                out.append(0)
            elif n_zeros == 1:
                if n == 0:
                    out.append(p)
                else:
                    out.append(0)
            else:
                out.append(p // n)
        return out
