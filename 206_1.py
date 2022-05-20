class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head, _ = self.reverse(head)
        return head

    def reverse(self, head):
        if not head:
            return None, None

        head_of_rest, tail_of_rest = self.reverse(head.next)

        if head_of_rest:
            head.next = None
            tail_of_rest.next = head
            tail_of_rest = tail_of_rest.next
            return head_of_rest, tail_of_rest

        return head, head
