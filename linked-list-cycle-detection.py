# linked list cycle detection
# https://neetcode.io/problems/linked-list-cycle-detection/question
# code by aveia@github

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head) -> bool:
        visited = set()
        p = head
        while p:
            if id(p) in visited:
                return True
            visited.add(id(p))
            p = p.next
        return False
