# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        h1 = None
        h1_tail = None
        h2 = None
        h2_tail = None

        p = head
        while p:
            n = p.next
            if p.val < x:
                if h1:
                    h1_tail.next = p
                else:
                    h1 = p
                h1_tail = p
            else:
                if h2:
                    h2_tail.next = p
                else:
                    h2 = p
                h2_tail = p

            p = n

        if h2_tail:
            h2_tail.next = None

        if not h1:
            return h2

        h1_tail.next = h2
        return h1
