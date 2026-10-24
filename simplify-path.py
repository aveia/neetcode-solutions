# simplify path
# https://neetcode.io/problems/simplify-path/question
# code by aveia@github

class Solution:
    def simplifyPath(self, path: str) -> str:
        xs = []
        for x in path.split('/'):
            if x in ['.', '']:
                continue
            elif x == '..':
                xs.pop() if xs else "i am root"
            else:
                xs.append(x)
        return '/' + '/'.join(xs)
