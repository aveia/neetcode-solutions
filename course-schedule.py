# course schedule
# https://neetcode.io/problems/course-schedule/question
# code by aveia@github

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        from collections import defaultdict
        visited: defaultdict[int, bool | str] = defaultdict(bool)

        adj_list = defaultdict(list)
        for a, b in prerequisites:
            adj_list[a].append(b)

        for course in range(numCourses):

            stack = [(course, False)]
            while stack:
                node, unstacking = stack.pop()

                if unstacking:
                    visited[node] = True
                    continue
                if visited[node] == 'stacked':
                    return False
                if visited[node]:
                    continue

                stack.append((node, True))
                visited[node] = 'stacked'
                for prereq in adj_list[node]:
                    stack.append((prereq, False))

        return True
