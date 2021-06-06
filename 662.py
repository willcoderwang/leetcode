# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        min_index_each_level = []
        max_index_each_level = []
        self.get_index(root, 0, 0, min_index_each_level, max_index_each_level)

        max_width = 0
        for i in range(len(min_index_each_level)):
            width = max_index_each_level[i] - min_index_each_level[i] + 1
            if width > max_width:
                max_width = width

        return max_width

    def get_index(self, node, index, level, min_index_each_level, max_index_each_level):
        if node is None:
            return

        if level >= len(min_index_each_level):
            min_index_each_level.append(index)
            max_index_each_level.append(index)
        else:
            max_index_each_level[level] = index

        self.get_index(node.left, index * 2 + 1, level + 1, min_index_each_level, max_index_each_level)
        self.get_index(node.right, index * 2 + 2, level + 1, min_index_each_level, max_index_each_level)
