# greatest common divisor of strings
# https://neetcode.io/problems/greatest-common-divisor-of-strings/question
# code by aveia@github

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        len1 = len(str1)
        len2 = len(str2)
        max_len = max(len1, len2)

        for i in range(1, max_len + 1):

            if max_len % i:
                continue

            d = max_len // i
            if not (len1 % d == 0 == len2 % d):
                continue

            rs = str1[:d] # repeating string
            mismatch = False
            for i in range(len1 // d):
                if str1[i * d:(i + 1) * d] != rs:
                    mismatch = True
            for i in range(len2 // d):
                if str2[i * d:(i + 1) * d] != rs:
                    mismatch = True

            if not mismatch:
                return rs

        return ''
