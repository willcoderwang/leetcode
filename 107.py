# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        the_queue = [root]
        the_queue_2 = []
        result = []

        while the_queue:
            temp = []
            while the_queue:
                node = the_queue.pop(0)
                temp.append(node.val)

                if node.left:
                    the_queue_2.append(node.left)
                if node.right:
                    the_queue_2.append(node.right)

            result.append(temp)
            the_queue = the_queue_2
            the_queue_2 = []

        result.reverse()

        return result