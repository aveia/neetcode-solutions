# word pattern
# https://neetcode.io/problems/word-pattern/question
# code by aveia@github

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        ss = s.split()
        if len(ss) != len(pattern):
            return False

        c2w, w2c = {}, {}
        for char, word in zip(pattern, ss):

            if char in c2w and c2w[char] != word:
                return False

            if word in w2c and w2c[word] != char:
                return False

            c2w[char] = word
            w2c[word] = char

        return True
