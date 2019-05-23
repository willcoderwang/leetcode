# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        ordered_nodes_list = self.get_ordered_nodes_list(root)

        ordered_nodes_list.reverse()

        current = 0
        for node in ordered_nodes_list:
            current += node.val
            node.val = current

        return root

    def get_ordered_nodes_list(self, root, ordered_nodes_list=None):
        if ordered_nodes_list is None:
            ordered_nodes_list = []

        if root.left:
            self.get_ordered_nodes_list(root.left, ordered_nodes_list)

        ordered_nodes_list.append(root)

        if root.right:
            self.get_ordered_nodes_list(root.right, ordered_nodes_list)

        return ordered_nodes_list
