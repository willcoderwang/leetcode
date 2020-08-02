# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        if len(nums) == 1:
            return TreeNode(nums[0], None, None)

        if len(nums) == 2:
            left_child = TreeNode(nums[0], None, None)
            root = TreeNode(nums[1], left_child, None)
            return root

        if len(nums) == 3:
            left_child = TreeNode(nums[0], None, None)
            right_child = TreeNode(nums[2], None, None)
            root = TreeNode(nums[1], left_child, right_child)
            return root

        mid = len(nums) // 2
        left_child = self.sortedArrayToBST(nums[:mid])
        right_child = self.sortedArrayToBST(nums[mid+1:])
        root = TreeNode(nums[mid], left_child, right_child)
        return root