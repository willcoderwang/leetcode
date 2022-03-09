# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        _, count = self.traverse(original, target, 0)
        res, _ = self.traverse_to(cloned, count, 0)
        return res

    def traverse(self, tree, target, count):
        if tree == target:
            return True, count

        if tree.left:
            got_there, count = self.traverse(tree.left, target, count + 1)
            if got_there:
                return got_there, count
        if tree.right:
            got_there, count = self.traverse(tree.right, target, count + 1)
            if got_there:
                return got_there, count

        return False, count

    def traverse_to(self, tree, target, count):
        if count == target:
            return tree, count

        if tree.left:
            found, count = self.traverse_to(tree.left, target, count + 1)
            if found:
                return found, count
        if tree.right:
            found, count = self.traverse_to(tree.right, target, count + 1)
            if found:
                return found, count

        return None, count
