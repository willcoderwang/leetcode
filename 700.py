# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        p = root
        while p:
            if p.val == val:
                return p
            elif p.val > val:
                p = p.left
            else:
                p = p.right

        return p