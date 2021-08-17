# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesCore(root, [])

    def goodNodesCore(self, root, stack):
        if not root:
            return 0

        current = 0
        if not stack or root.val >= max(stack):
            current = 1

        stack.append(root.val)

        left = self.goodNodesCore(root.left, stack)

        right = self.goodNodesCore(root.right, stack)

        stack.pop()

        return current + left + right
