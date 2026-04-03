# course schedule ii
# https://neetcode.io/problems/course-schedule-ii/question
# code by aveia@github

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        reqs = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            reqs[a].append(b)

        taken = {}
        sequence = []

        def dfs(src):

            stack = [src]

            while stack:
                cur = stack.pop()

                if cur not in taken:
                    taken[cur] = False

                elif taken[cur] == False:
                    taken[cur] = True
                    sequence.append(cur)
                    continue

                elif taken[cur] == True:
                    continue

                stack.append(cur)

                for req in reqs[cur]:

                    if req in taken and taken[req] == False:
                        return False

                    stack.append(req)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return sequence
