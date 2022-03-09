# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head, new_tail = None, None
        p = head
        while p:
            n = p.next
            if n is not None and n.val == p.val:
                while n:
                    if n.val != p.val:
                        break
                    n = n.next
            else:
                if new_head is None:
                    new_head = p
                    new_tail = p
                else:
                    new_tail.next = p
                    new_tail = p
                new_tail.next = None
            p = n
        return new_head
