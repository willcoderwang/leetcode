# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLinkLength(self, head):
        length = 0
        p = head
        while p:
            length += 1
            p = p.next

        return length

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a_length = self.getLinkLength(headA)
        b_length = self.getLinkLength(headB)

        p_a = headA
        p_b = headB
        diff = a_length - b_length

        if diff > 0:
            for i in range(diff):
                p_a = p_a.next
        elif diff < 0:
            for i in range(-diff):
                p_b = p_b.next

        while p_a:
            if p_a == p_b:
                return p_a

            p_a = p_a.next
            p_b = p_b.next

        return None
