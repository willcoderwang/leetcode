# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        add_one = 0
        p1 = l1
        p2 = l2
        head = None
        tail = None

        while p1 or p2:
            n1 = p1.val if p1 else 0
            n2 = p2.val if p2 else 0

            s = n1 + n2 + add_one
            if s >= 10:
                add_one = 1
            else:
                add_one = 0

            new_node = ListNode(s % 10)
            if head:
                tail.next = new_node
            else:
                head = new_node

            tail = new_node

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        if add_one:
            new_node = ListNode(1)
            tail.next = new_node

        return head
