# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        res = lists[0]
        for i in range(1, len(lists)):
            res = self.merge_2_lists(res, lists[i])

        return res

    def merge_2_lists(self, list1, list2):
        dummy = ListNode()
        new_tail = dummy

        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val <= p2.val:
                new_tail.next = p1
                new_tail = new_tail.next
                p1 = p1.next
            else:
                new_tail.next = p2
                new_tail = new_tail.next
                p2 = p2.next

        if not p1:
            new_tail.next = p2
        else:
            new_tail.next = p1

        return dummy.next
