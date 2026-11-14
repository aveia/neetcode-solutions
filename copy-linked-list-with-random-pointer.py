# copy linked list with random pointer
# https://neetcode.io/problems/copy-linked-list-with-random-pointer/question
# code by aveia@github

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head):

        old2new = {None: None}
        last = Node(-1) # dummy node to avoid an `if`

        it = head
        while it is not None: # shenanigans on the next line, beware
            old2new[it] = last.next = last = Node(it.val)
            it = it.next

        it = head
        while it is not None:
            old2new[it].random = old2new[it.random]
            it = it.next

        return old2new[head]
