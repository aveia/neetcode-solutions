# decode string
# https://neetcode.io/problems/decode-string/question
# code by aveia@github

class Solution:
    def decodeString(self, s: str) -> str:
        i, n = 0, len(s)

        def decode():
            nonlocal i
            if i >= n:
                return ''

            if '0' <= s[i] <= '9':
                k = ''
                while '0' <= s[i] <= '9':
                    k += s[i]
                    i += 1
                k = int(k)
                i += 1 # consume '['
                ss = k * decode()
                i += 1 # consume ']'
                ss += decode()
                return ss

            elif 'a' <= s[i] <= 'z':
                ss = ''
                while i < n and 'a' <= s[i] <= 'z':
                    ss += s[i]
                    i += 1
                ss += decode()
                return ss

            return ''

        return decode()
