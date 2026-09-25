# longest common prefix
# https://neetcode.io/problems/longest-common-prefix/question
# code by aveia@github

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        from functools import reduce
        prefix = ''
        min_len = reduce(lambda a, b: min(a, len(b)), strs[1:], len(strs[0]))
        for i in range(min_len):
            eq = reduce(lambda a, b: a and b,
                    map(lambda x: x[i] == strs[0][i], strs[1:]),
                    True)
            if eq:
                prefix += strs[0][i]
            else:
                break
        return prefix
