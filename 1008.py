# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:
        nodes = [TreeNode(x) for x in preorder]

        current = None
        root = None
        stack = []

        for node in nodes:

            if current is None:
                root = node
                current = node
                continue

            if node.val < current.val:
                current.left = node
                stack.append(current)

                current = node
            else:
                pop = None
                while stack and stack[-1].val < node.val:
                    pop = stack.pop()

                if pop:
                    current = pop
                current.right = node
                current = node
                stack.append(current)

        return root
