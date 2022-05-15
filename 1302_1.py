# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        node_q = [root]
        level_sum = root.val

        while node_q:
            level_sum = 0
            new_node_q = []

            for n in node_q:
                level_sum += n.val
                if n.left:
                    new_node_q.append(n.left)
                if n.right:
                    new_node_q.append(n.right)

            node_q = new_node_q

        return level_sum
