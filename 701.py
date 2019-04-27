# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return root

        try_node = root
        parent = None
        left_child = True

        while try_node:
            parent = try_node
            if try_node.val > val:
                try_node = try_node.left
                left_child = True
            else:
                try_node = try_node.right
                left_child = False

        if left_child:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)

            return root
