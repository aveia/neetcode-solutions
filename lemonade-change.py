# lemonade change
# https://neetcode.io/problems/lemonade-change/question
# code by aveia@github

class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        from math import log

        counter = [0, 0, 0]
        for bill in bills:

            counter[round(log(bill // 5, 2))] += 1

            if bill == 10:
                if counter[0]:
                    counter[0] -= 1
                else:
                    return False

            elif bill == 20:
                if counter[0] and counter[1]:
                    counter[0] -= 1
                    counter[1] -= 1
                elif counter[0] >= 3:
                    counter[0] -= 3
                else:
                    return False

        return True
