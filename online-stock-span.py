# online stock span
# https://neetcode.io/problems/online-stock-span/question
# code by aveia@github

# TODO: make it nicer

class StockSpanner:

    def __init__(self):
        self.xs = []
        self.last = None

    def next(self, price: int) -> int:

        if self.last is None:
            self.last = price
            return 1

        self.xs.append(price - self.last)
        self.last = price

        s = 0
        qty = 1
        i = len(self.xs) - 1
        while i >= 0:
            s += self.xs[i]
            if s < 0:
                break
            qty += 1
            i -= 1

        return qty
