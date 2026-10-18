# verifying an alien dictionary
# https://neetcode.io/problems/verifying-an-alien-dictionary/question
# code by aveia@github

class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        pos = {}
        for i, c in enumerate(order):
            pos[c] = i

        def gt(w1, w2):
            l = min(len(w1), len(w2))
            for i in range(l):
                if pos[w1[i]] > pos[w2[i]]:
                    return True
                elif pos[w1[i]] < pos[w2[i]]:
                    return False
            return len(w1) > len(w2)

        for i in range(len(words) - 1):
            if gt(words[i], words[i + 1]):
                return False
        return True
