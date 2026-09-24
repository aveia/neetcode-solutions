# design hashset
# https://neetcode.io/problems/design-hashset/question
# code by aveia@github

# TODO: improve it

class MyHashSet:

    def __init__(self):
        self.table_width = 2 ** 15 - 1
        self.table = [[] for _ in range(self.table_width)]

    def add(self, key: int) -> None:
        idx = hash(key) % self.table_width
        t = self.table[idx]
        found = any(map(lambda x: x == key, t))
        t.append(key) if not found else None

    def remove(self, key: int) -> None:
        idx = hash(key) % self.table_width
        t = self.table[idx]
        for i, k in enumerate(t):
            if k == key:
                t.pop(i)
                return

    def contains(self, key: int) -> bool:
        idx = hash(key) % self.table_width
        t = self.table[idx]
        return any(map(lambda x: x == key, t))
