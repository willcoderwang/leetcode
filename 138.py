"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return

        index = 0
        node_to_index = dict()
        node_to_index[head] = 0
        index += 1

        new_nodes = []
        new_head = Node(head.val)
        new_nodes.append(new_head)

        pre = head
        new_pre = new_head
        p = head.next
        while p:
            new_p = Node(p.val)
            new_pre.next = new_p
            new_nodes.append(new_p)
            node_to_index[p] = index
            index += 1

            pre = p
            new_pre = new_p
            p = p.next

        p = head
        new_p = new_head
        while p:
            if p.random:
                new_p.random = new_nodes[node_to_index[p.random]]

            p = p.next
            new_p = new_p.next

        return new_head
