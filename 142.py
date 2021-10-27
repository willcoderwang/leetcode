# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        p1 = head
        p2 = head

        step = 0
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next
            p2 = p2.next

            step += 1
            if p1 == p2:
                break
        else:
            return None

        p1 = head
        p2 = head
        for i in range(step):
            p2 = p2.next

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1
