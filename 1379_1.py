# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return self.traverse(original, cloned, target)

    def traverse(self, original, cloned, target):
        if not original:
            return

        if original == target:
            return cloned

        return self.traverse(original.left, cloned.left, target) or self.traverse(original.right, cloned.right, target)
