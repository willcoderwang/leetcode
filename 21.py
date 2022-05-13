class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        new_head, new_tail = None, None

        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val <= p2.val:
                if new_head:
                    new_tail.next = p1
                else:
                    new_head = p1
                new_tail = p1
                p1 = p1.next
            else:
                if new_head:
                    new_tail.next = p2
                else:
                    new_head = p2
                new_tail = p2
                p2 = p2.next

        if not p1:
            new_tail.next = p2
        elif not p2:
            new_tail.next = p1

        return new_head
