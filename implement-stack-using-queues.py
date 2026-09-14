# implement stack using queues
# https://neetcode.io/problems/implement-stack-using-queues/question
# code by aveia@github

# TODO: make it prettier

class MyStack:

    def __init__(self):
        from collections import deque
        self.q1 = deque()
        self.q2 = deque()
        self.q1_active = True

    def push(self, x: int) -> None:
        q = self.q1 if self.q1_active else self.q2
        q.append(x)

    def pop(self) -> int:
        q, other_q = (self.q1, self.q2) if self.q1_active else (self.q2, self.q1)
        for _ in range(len(q) - 1):
            other_q.append(q.popleft())
        self.q1_active = not self.q1_active
        return q.popleft()

    def top(self) -> int:
        q, other_q = (self.q1, self.q2) if self.q1_active else (self.q2, self.q1)
        for _ in range(len(q) - 1):
            other_q.append(q.popleft())
        self.q1_active = not self.q1_active
        ret = q[0]
        other_q.append(q.popleft())
        return ret

    def empty(self) -> bool:
        return not (self.q1 or self.q2)
