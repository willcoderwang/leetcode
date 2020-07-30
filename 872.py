# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.get_leves(root1) == self.get_leves(root2)

    def get_leves(self, root):
        if not root.left and not root.right:
            return [root.val]

        res = []
        if root.left:
            res.extend(self.get_leves(root.left))

        if root.right:
            res.extend(self.get_leves(root.right))

        return res