# merge two sorted linked lists
# https://neetcode.io/problems/merge-two-sorted-linked-lists/question
# code by aveia@github

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        prev = dummy

        while list1 or list2:

            if list1 and list2 and list1.val < list2.val or not list2:
                cur = ListNode(list1.val)
                list1 = list1.next
            else:
                cur = ListNode(list2.val)
                list2 = list2.next

            prev.next = cur
            prev = cur

        return dummy.next
