# valid palindrome ii
# https://neetcode.io/problems/valid-palindrome-ii/question
# code by aveia@github

# TODO: analyze complexity and improve solution

class Solution:
    def validPalindrome(self, s: str) -> bool:

        def valid(i, j, skipped=False):
            if i >= j:
                return True
            if s[i] == s[j] and valid(i + 1, j - 1, skipped):
                return True
            if  not skipped and (valid(i + 1, j, True) or valid(i, j - 1, True)):
                return True
            return False

        return valid(0, len(s) - 1)
