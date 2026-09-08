# add binary
# https://neetcode.io/problems/add-binary/question
# code by aveia@github

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        a = a[::-1]
        b = b[::-1]

        if len(b) < len(a):
            a, b = b, a

        a += '0' * (len(b) - len(a))

        carry, res = '0', ''
        for x, y in zip(a, b):
            if x == y:
                res += carry
                carry = x
            else:
                res += '0' if carry == '1' else '1'

        if carry == '1':
            res += '1'

        return res[::-1]
