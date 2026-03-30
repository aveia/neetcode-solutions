# evaluate reverse polish notation
# https://neetcode.io/problems/evaluate-reverse-polish-notation/question
# code by aveia@github

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        op = {
            '+': lambda a, b: b + a,
            '-': lambda a, b: b - a,
            '*': lambda a, b: b * a,
            '/': lambda a, b: int(b / a),
        }
        stack = []
        for tok in tokens:
            if tok in op:
                stack.append(op[tok](stack.pop(), stack.pop()))
            else:
                stack.append(int(tok))
        return stack.pop()
