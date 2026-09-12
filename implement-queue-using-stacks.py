# implement queue using stacks
# https://neetcode.io/problems/implement-queue-using-stacks/question
# code by aveia@github

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def move_right(self):
        while self.s1:
            self.s2.append(self.s1.pop())

    def move_left(self):
        while self.s2:
            self.s1.append(self.s2.pop())

    def push(self, x: int) -> None:
        if self.s1:
            self.move_right()
        self.s2.append(x)

    def pop(self) -> int:
        if self.s2:
            self.move_left()
        return self.s1.pop()

    def peek(self) -> int:
        if self.s2:
            self.move_left()
        return self.s1[-1]

    def empty(self) -> bool:
        return not (self.s1 or self.s2)
