# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        stack1 = [root]
        stack2 = []
        result = []

        while True:
            if not stack1:
                break
            temp_res = []
            while stack1:
                node = stack1.pop()
                temp_res.append(node.val)
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)

            result.append(temp_res)

            if not stack2:
                break
            temp_res = []
            while stack2:
                node = stack2.pop()
                temp_res.append(node.val)
                if node.right:
                    stack1.append(node.right)
                if node.left:
                    stack1.append(node.left)

            result.append(temp_res)

        return result