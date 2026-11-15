# lfu cache
# https://neetcode.io/problems/lfu-cache/question
# code by aveia@github

class LFUCache:

    def left(self, i): return 2 * i + 1
    def right(self, i): return 2 * i + 2
    def parent(self, i): return (i - 1) // 2

    def sift_up(self, i):
        p = self.parent(i)
        while i and i != p and self.heap[i] < self.heap[p]:
            self.heap_idx[self.heap[i][2]] = p
            self.heap_idx[self.heap[p][2]] = i
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p
            p = self.parent(i)
        return i

    def min_idx(self, *idxs):
        mi = idxs[0]
        for idx in idxs[1:]:
            if idx < len(self.heap) and self.heap[idx] < self.heap[mi]:
                mi = idx
        return mi

    def sift_down(self, i):
        l, r = self.left(i), self.right(i)
        m = self.min_idx(i, l, r)
        if m == i:
            return i
        self.heap_idx[self.heap[i][2]] = m
        self.heap_idx[self.heap[m][2]] = i
        self.heap[i], self.heap[m] = self.heap[m], self.heap[i]
        return self.sift_down(m)

    def __init__(self, capacity: int):
        self.heap = []
        self.cache = {}
        self.heap_idx = {}
        self.op_count = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        i = self.heap_idx[key]
        self.heap[i][0] += 1
        self.heap[i][1] = self.op_count
        self.op_count += 1
        self.heap_idx[key] = self.sift_down(i)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            i = self.heap_idx[key]
            self.heap[i][0] += 1
            self.heap[i][1] = self.op_count
            self.sift_down(i)

        elif len(self.cache) == self.capacity:
            _, _, old_key = self.heap[0]
            del self.cache[old_key]
            del self.heap_idx[old_key]
            self.heap[0] = [1, self.op_count, key]
            self.heap_idx[key] = 0
            self.sift_down(0)

        else:
            self.heap.append([1, self.op_count, key])
            self.heap_idx[key] = len(self.heap) - 1
            self.sift_up(len(self.heap) - 1)

        self.op_count += 1
        self.cache[key] = value
