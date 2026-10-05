# excel sheet column title
# https://neetcode.io/problems/excel-sheet-column-title/question
# code by aveia@github

# TODO: explain it

class Solution:

    # def convertToTitle(self, n: int) -> str:
    #     title = ''
    #     n -= 1
    #     n, r = n // 26, n % 26
    #     title += chr(ord('A') + r)
    #     while n:
    #         n -= 1
    #         n, r = n // 26, n % 26
    #         title += chr(ord('A') + r)
    #     return title[::-1]

    def convertToTitle(self, n: int) -> str:
        title = ''
        n -= 1
        n, r = n // 26, n % 26
        while n:
            n -= 1
            title += chr(ord('A') + r)
            n, r = n // 26, n % 26
        title += chr(ord('A') + r)
        return title[::-1]
