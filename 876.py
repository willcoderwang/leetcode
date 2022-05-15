class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p_fast = head
        p_slow = head

        while p_fast and p_fast.next:
            p_fast = p_fast.next
            p_fast = p_fast.next
            p_slow = p_slow.next

        return p_slow
