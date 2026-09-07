# letter combinations of a phone number
# https://neetcode.io/problems/combinations-of-a-phone-number/question
# code by aveia@github

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        letters = {
            '2': 'abc', '3': 'def',
            '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
        }

        def combinations(digits):
            if not digits:
                return []
            if len(digits) == 1:
                return list(letters[digits])
            res = []
            for letter in letters[digits[0]]:
                for comb in combinations(digits[1:]):
                    res.append(letter + comb)
            return res

        return combinations(digits)
