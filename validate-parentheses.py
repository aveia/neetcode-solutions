# valid parentheses
# https://neetcode.io/problems/validate-parentheses/question
# code by aveia@github

class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            elif not stack or stack[-1] != match[c]:
                return False
            else:
                stack.pop()
        return not stack
