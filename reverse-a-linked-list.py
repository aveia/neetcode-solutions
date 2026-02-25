# reverse linked list
# https://neetcode.io/problems/reverse-a-linked-list/question
# code by aveia@github

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        if not head:
            return None
        p = head
        prev = None
        while p.next:
            n = p.next
            p.next = prev
            prev = p
            p = n
        p.next = prev
        return p
