# remove nth node from end of list
# https://neetcode.io/problems/remove-node-from-end-of-linked-list/question
# code by aveia@github

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        fast = head
        slow = head
        for _ in range(n):
            fast = fast.next
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        if prev is None:
            return head.next
        prev.next = prev.next.next
        return head
