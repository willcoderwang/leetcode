# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = head
        for i in range(n):
            p = p.next

        if not p:
            return head.next

        p2 = head
        while p.next:
            p = p.next
            p2 = p2.next

        p2.next = p2.next.next

        return head
