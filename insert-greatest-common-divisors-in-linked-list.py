# insert greatest common divisors in linked list
# https://neetcode.io/problems/insert-greatest-common-divisors-in-linked-list/question
# code by aveia@github

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import math as m

        def gcd(a, b):
            divs_a, divs_b = set(), set()
            for i in range(1, int(m.sqrt(a)) + 1):
                if a % i == 0:
                    divs_a.add(i)
                    divs_a.add(a // i)
            for i in range(1, int(m.sqrt(b)) + 1):
                if b % i == 0:
                    divs_b.add(i)
                    divs_b.add(b // i)
            common = divs_a & divs_b
            if len(common) == 1:
                return common.pop()
            return max(*common)

        cur = head
        while cur and cur.next:
            d = gcd(cur.val, cur.next.val)
            cur.next = ListNode(d, cur.next)
            cur = cur.next.next

        return head
