# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p1 = head
        if p1 is None:
            return p1
        p2 = p1.next
        if p2 is None:
            return p1
        p1.next = None
        while p2:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3

        return p1