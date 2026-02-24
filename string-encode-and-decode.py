# encode and decode strings
# https://neetcode.io/problems/string-encode-and-decode/question
# code by aveia@github

class Solution:

    def encode(self, strs: list[str]) -> str:
        return ''.join(s.replace('@', '@@').replace(':', '@:') + ':' for s in strs)

    def decode(self, s: str) -> list[str]:
        strs = []
        cur = ''
        i = 0
        while i < len(s):
            if s[i] == ':':
                strs.append(cur)
                cur = ''
            elif s[i] == '@':
                cur += s[i + 1]
                i += 1
            else:
                cur += s[i]
            i += 1
        return strs
