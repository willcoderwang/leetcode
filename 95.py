# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n < 1:
            return None

        first_node = TreeNode(1)
        if n == 1:
            return [first_node]

        pre_results = [first_node]
        for i in range(2, n+1):
            results = []
            for pre_r in pre_results:
                node = TreeNode(i, left=pre_r)
                results.append(node)

                p = pre_r
                while True:
                    pre_copy_root, right_most = Solution.copy_subtree(pre_r, p)
                    pre_copy_left, _ = Solution.copy_subtree(p.right)
                    node = TreeNode(i, left=pre_copy_left)
                    right_most.right = node

                    results.append(pre_copy_root)

                    p = p.right
                    if p is None:
                        break

            pre_results = results

        return pre_results

    @staticmethod
    def copy_subtree(root, stop=None):
        if root is None:
            return None, None

        left = None
        right = None
        right_most = None
        if root.left:
            left, _ = Solution.copy_subtree(root.left)
        if root != stop and root.right:
            right, child_right_most = Solution.copy_subtree(root.right, stop)
            if child_right_most:
                right_most = child_right_most
        new_root = TreeNode(root.val, left, right)
        if right_most is None:
            right_most = new_root

        return new_root, right_most