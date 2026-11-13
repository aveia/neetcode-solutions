# minimum array end
# https://neetcode.io/problems/minimum-array-end/question
# code by aveia@github

class Solution:
    def minEnd(self, n: int, x: int) -> int:

        x_bits = f'{x:b}'[::-1]
        list_of_0_bits = []

        j = 0
        last_1_bit = -1
        for i, bit in enumerate(x_bits):
            if int(bit):
                last_1_bit = i
                continue
            list_of_0_bits.append(i)
            j += 1

        k = x
        n_minus_1_bits = f'{n - 1:b}'[::-1]
        for m, bit in enumerate(n_minus_1_bits):
            if int(bit):
                if m < len(list_of_0_bits):
                    k |= 2 ** list_of_0_bits[m]
                else:
                    k |= 2 ** (last_1_bit + 1 + (m - len(list_of_0_bits)))

        return k
