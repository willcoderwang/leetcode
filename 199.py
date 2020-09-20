# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        results = []
        self.postOrder(root, 0, results)

        return results

    def postOrder(self, root, level, results):
        if root.left:
            self.postOrder(root.left, level + 1, results)
        if root.right:
            self.postOrder(root.right, level + 1, results)

        if not len(results) > level:
            results.extend([None] * (level + 1 - len(results)))

        results[level] = root.val
