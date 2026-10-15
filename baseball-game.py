# baseball game
# https://neetcode.io/problems/baseball-game/question
# code by aveia@github

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        scores = []
        for op in operations:
            try:
                scores.append(int(op))
            except:
                if op == '+':
                    scores.append(scores[-1] + scores[-2])
                elif op == 'D':
                    scores.append(2 * scores[-1])
                else:
                    scores.pop()
        return sum(scores)
