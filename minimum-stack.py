# min stack
# https://neetcode.io/problems/minimum-stack/question
# code by aveia@github

class MinStack:

    class Node:
        def __init__(self, val, min_, next_):
            self.val = val
            self.min = min_
            self.next = next_

    def __init__(self):
        self.stack = None

    def min(self, val):
        if self.stack is None:
            return val
        return min(self.stack.min, val)

    def push(self, val: int) -> None:
        self.stack = MinStack.Node(val, self.min(val), self.stack)

    def pop(self) -> None:
        self.stack = self.stack.next

    def top(self) -> int:
        return self.stack.val

    def getMin(self) -> int:
        return self.stack.min
