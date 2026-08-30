# permutation in string
# https://neetcode.io/problems/permutation-string/question
# code by aveia@github

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        from collections import defaultdict

        h1 = defaultdict(int)
        for c in s1:
            h1[c] += 1

        h2 = defaultdict(int)
        for c in s2[:len(s1)]:
            h2[c] += 1

        if h1 == h2:
            return True

        for i in range(len(s2) - len(s1)):

            h2[s2[i]] -= 1
            if h2[s2[i]] == 0:
                del h2[s2[i]]
            h2[s2[i + len(s1)]] += 1

            if h1 == h2:
                return True

        return False
