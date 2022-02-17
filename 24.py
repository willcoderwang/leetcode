# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = head.next
        new_tail = head

        i = head
        while i and i.next:
            the_rest = i.next.next

            i.next.next = i
            new_tail.next = i.next
            new_tail = i
            new_tail.next = the_rest

            i = the_rest

        return new_head
