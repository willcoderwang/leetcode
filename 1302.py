# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        _, the_sum = self.deepestLeavesSumCore(root, 0, 0, root.val)

        return the_sum

    def deepestLeavesSumCore(self, node, current_depth, current_max_depth, the_sum):
        current_max_depth, the_sum = self.visitNode(node, current_depth, current_max_depth, the_sum)

        if node.left:
            current_max_depth, the_sum = self.deepestLeavesSumCore(node.left, current_depth + 1, current_max_depth,
                                                                   the_sum)
        if node.right:
            current_max_depth, the_sum = self.deepestLeavesSumCore(node.right, current_depth + 1, current_max_depth,
                                                                   the_sum)

        return current_max_depth, the_sum

    def visitNode(self, node, current_depth, current_max_depth, the_sum):
        if current_depth > current_max_depth:
            current_max_depth = current_depth
            the_sum = node.val
        elif current_depth == current_max_depth:
            the_sum += node.val

        return current_max_depth, the_sum
