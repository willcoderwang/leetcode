class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        new_tail = dummy

        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val <= p2.val:
                new_tail.next = p1
                new_tail = p1
                p1 = p1.next
            else:
                new_tail.next = p2
                new_tail = p2
                p2 = p2.next

        if not p1:
            new_tail.next = p2
        elif not p2:
            new_tail.next = p1

        return dummy.next
