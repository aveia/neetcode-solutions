# reverse bits
# https://neetcode.io/problems/reverse-bits/question
# code by aveia@github

class Solution:
    def reverseBits(self, n: int) -> int:
        bits = [n % 2]
        n //= 2
        while n > 0:
            bits.append(n % 2)
            n //= 2

        while len(bits) < 32:
            bits.append(0)

        k = 0
        for i, b in enumerate(bits):
            k += b * 2 ** (31 - i)
        return k
