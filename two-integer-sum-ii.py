# two integer sum ii
# https://neetcode.io/problems/two-integer-sum-ii/question
# code by aveia@github

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            s = numbers[j] + numbers[i]
            if s == target:
                return [i + 1, j + 1]
            elif s > target:
                j -= 1
            else:
                i += 1
