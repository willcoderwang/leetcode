# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        results = []
        queue = [root]

        while True:
            children_queue = []
            res = []
            while queue:
                node = queue[0]
                del queue[0]
                res.append(node.val)
                if node.left:
                    children_queue.append(node.left)
                if node.right:
                    children_queue.append(node.right)

            results.append(res)
            queue = children_queue

            if not queue:
                break

        return results