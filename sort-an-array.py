# sort an array
# https://neetcode.io/problems/sort-an-array/question
# code by aveia@github

class Solution:
    def sortArray(self, xs: List[int]) -> List[int]:

        def left(i):
            return i * 2

        def right(i):
            return i * 2 + 1

        def max_i(xs, n, *idxs):
            if not idxs:
                return None
            mi = idxs[0] if idxs[0] < n else None
            for i in idxs[1:]:
                if i < n and xs[i] > xs[mi]:
                    mi = i
            return mi

        def sift_up(xs, i):
            while i > 0:
                up_i = i // 2
                if xs[i] > xs[up_i]:
                    xs[i], xs[up_i] = xs[up_i], xs[i]
                    i = up_i
                else:
                    return

        def sift_down(xs, n):
            if n < 2:
                return
            i = 0
            while i < n:
                mi = max_i(xs, n, i, left(i), right(i))
                if i == mi:
                    return
                xs[i], xs[mi] = xs[mi], xs[i]
                i = mi

        def heapify(xs):
            for i in range(len(xs)):
                sift_up(xs, i)

        heapify(xs)
        for i in range(len(xs) - 1, 0, -1):
            xs[0], xs[i] = xs[i], xs[0]
            sift_down(xs, i)
        return xs
