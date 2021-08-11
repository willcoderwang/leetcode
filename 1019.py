# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        p = head
        results = []
        stack = []
        i = 0
        while p.next:
            if p.next.val > p.val:
                results.append(p.next.val)
                while len(stack) > 0 and stack[-1][1] < p.next.val:
                    index, _ = stack.pop()
                    results[index] = p.next.val

            else:
                results.append(0)
                stack.append((i, p.val))
            p = p.next
            i += 1

        results.append(0)

        return results