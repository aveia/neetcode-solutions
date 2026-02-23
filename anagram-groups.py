# group anagrams
# https://neetcode.io/problems/anagram-groups/question
# code by aveia@github

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        from collections import defaultdict
        anagrams = defaultdict(list)
        for s in strs:
            anagrams[tuple(sorted(s))].append(s)
        return list(anagrams.values())
