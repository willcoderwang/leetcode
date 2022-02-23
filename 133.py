"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        new_graph_nodes = dict()
        visited = []

        def dfs(node):
            if node.val in visited:
                return

            if node.val in new_graph_nodes:
                new_node = new_graph_nodes[node.val]
            else:
                new_node = Node(node.val)
                new_graph_nodes[node.val] = new_node

            for n in node.neighbors:
                if n.val in new_graph_nodes:
                    new_node.neighbors.append(new_graph_nodes[n.val])
                else:
                    new_neighbor = Node(n.val)
                    new_graph_nodes[n.val] = new_neighbor
                    new_node.neighbors.append(new_neighbor)

            visited.append(node.val)

            for n in node.neighbors:
                dfs(n)

        dfs(node)

        return new_graph_nodes[node.val]
