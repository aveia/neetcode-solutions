# daily temperatures
# https://neetcode.io/problems/daily-temperatures/question
# code by aveia@github

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        result = [0 for _ in temperatures]
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                i0, t0 = stack.pop()
                result[i0] = i - i0
            stack.append((i, t))
        return result
