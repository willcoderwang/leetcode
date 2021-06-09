# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        flip_nodes = []
        stack = []
        cursor = root
        vi = 0
        while cursor:
            if cursor.val != voyage[vi]:
                return [-1]

            vi += 1
            if cursor.left is None and cursor.right is None:
                if stack:
                    cursor = stack.pop()
                else:
                    return flip_nodes

            elif cursor.left is not None and cursor.right is None:
                cursor = cursor.left

            elif cursor.left is None and cursor.right is not None:
                cursor = cursor.right
            else:

                if cursor.left.val == voyage[vi]:
                    stack.append(cursor.right)
                    cursor = cursor.left
                elif cursor.right.val == voyage[vi]:
                    flip_nodes.append(cursor.val)
                    stack.append(cursor.left)
                    cursor = cursor.right
                else:
                    return [-1]
