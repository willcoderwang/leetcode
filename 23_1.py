# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        dummy = ListNode()
        new_tail = dummy

        h = []
        for i, l in enumerate(lists):
            if l:
                heappush(h, (l.val * 10000 + i, l))

        while len(h) > 1:
            v, p = heappop(h)
            new_tail.next = p
            new_tail = new_tail.next

            if p.next:
                i = v % 10000
                heappush(h, (p.next.val * 10000 + i, p.next))

        if h:
            new_tail.next = h[0][1]
            new_tail = new_tail.next

        return dummy.next
