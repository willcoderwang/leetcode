# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        _, _, result = self.sumEvenGrandparentCore(root, 0)
        return result

    def sumEvenGrandparentCore(self, root, result):
        if not root.left and not root.right:
            return 0, 0, result

        child_sum = 0
        grandchild_sum = 0
        if root.left:
            child_sum += root.left.val
            left_child_sum, _, result = self.sumEvenGrandparentCore(root.left, result)
            grandchild_sum += left_child_sum

        if root.right:
            child_sum += root.right.val
            right_child_sum, _, result = self.sumEvenGrandparentCore(root.right, result)
            grandchild_sum += right_child_sum

        if root.val % 2 == 0:
            result += grandchild_sum

        return child_sum, grandchild_sum, result