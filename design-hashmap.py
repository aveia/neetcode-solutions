# design hashmap
# https://neetcode.io/problems/design-hashmap/question
# code by aveia@github

# TODO: improve it

class MyHashMap:

    def __init__(self):
        self.table_width = 2 ** 15 - 1
        self.table = [[] for _ in range(self.table_width)]
        self.keys = set()

    def insert(self, key, val, idx):
        t = self.table[idx]
        t.extend([None])
        i = len(t) - 1 # invariant: t[i] is safe to overwrite
        while i - 1 >= 0 and t[i - 1][0] > key:
            t[i] = t[i - 1]
            i -= 1
        self.keys.add(key)
        t[i] = (key, val)

    def set(self, key, val, idx):
        t = self.table[idx]
        for i in range(len(t)):
            if key == t[i][0]:
                t[i] = (key, val)
                return

    def put(self, key: int, val: int) -> None:
        idx = hash(key) % self.table_width
        if key in self.keys:
            self.set(key, val, idx)
        else:
            self.insert(key, val, idx)

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        idx = hash(key) % self.table_width
        t = self.table[idx]
        for k, v in t:
            if k == key:
                return v

    def remove(self, key: int) -> None:
        if key not in self.keys:
            return
        self.keys.remove(key)
        idx = hash(key) % self.table_width
        t = self.table[idx]
        for i in range(len(t)):
            if t[i][0] == key:
                t.pop(i)
                return
