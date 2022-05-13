class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        node_q = [root]

        while node_q:
            new_node_q = []
            for i in range(len(node_q)):
                if i + 1 < len(node_q):
                    node_q[i].next = node_q[i + 1]

                if node_q[i].left:
                    new_node_q.append(node_q[i].left)
                if node_q[i].right:
                    new_node_q.append(node_q[i].right)

            node_q = new_node_q

        return root
