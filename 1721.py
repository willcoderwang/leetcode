# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        p1 = head
        for _ in range(k - 1):
            p1 = p1.next
        p2 = head
        end = p1
        while end.next:
            p2 = p2.next
            end = end.next

        p1.val, p2.val = p2.val, p1.val

        return head