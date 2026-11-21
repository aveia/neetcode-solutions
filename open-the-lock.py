# open the lock
# https://neetcode.io/problems/open-the-lock/question
# code by aveia@github

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        from collections import deque
        from itertools import product

        deadends_set = set(deadends)
        appended = {'0000'}
        q = deque([('0000', 0)])

        while q:
            code, distance = q.popleft()

            if code == target:
                return distance

            if code in deadends_set:
                continue

            for i, d in product(range(4), [1, -1]):
                new_digit = chr((int(code[i]) + d) % 10 + ord('0'))
                new_code = code[:i] + new_digit + code[i+1:]

                if new_code not in appended:
                    q.append((new_code, distance + 1))
                    appended.add(new_code)

        return -1
