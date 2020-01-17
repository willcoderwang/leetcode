# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        index = head
        while index:
            result = result * 2 + index.val
            index = index.next

        return result