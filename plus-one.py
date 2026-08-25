# plus one
# https://neetcode.io/problems/plus-one/question
# code by aveia@github

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()

        i, n = 0, len(digits)
        digits[0] += 1
        while digits[i] >= 10:
            digits[i] = 0
            i += 1
            if i == n:
                digits.append(1)
                break
            digits[i] += 1

        digits.reverse()
        return digits
