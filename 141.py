# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cnt = 0
        p = head
        while p:
            cnt += 1
            p = p.next
            if cnt > 10001:
                return True

        return False
