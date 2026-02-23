# valid palindrome
# https://neetcode.io/problems/is-palindrome/question
# code by aveia@github

class Solution:
    def isPalindrome(self, s: str) -> bool:

        def valid(c):
            if ('0' <= c <= '9') or ('a' <= c <= 'z'):
                return True
            return False

        l = list(filter(valid, s.lower()))

        if l == list(reversed(l)):
            return True
        return False
