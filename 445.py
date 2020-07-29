# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self._link_to_int(l1)
        num2 = self._link_to_int(l2)

        res = num1 + num2

        return self._int_to_link(res)

    def _link_to_int(self, link):
        num = 0
        p = link
        while p:
            num = num * 10 + p.val
            p = p.next
        return num

    def _int_to_link(self, num):
        if num == 0:
            p = ListNode()
            return p

        p = None

        while num:
            remain = num % 10
            num //= 10
            node = ListNode(remain, p)
            p = node

        return p
