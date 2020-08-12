/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        int[] pre_index = {0};
        return buildTreeCore(preorder, inorder, pre_index, 0, inorder.length-1);
    }

    private TreeNode buildTreeCore(int[] preorder, int[] inorder, int[] pre_index, int start, int stop) {
        if (start > stop)
            return null;

        if (start == stop) {
            ++pre_index[0];
            return new TreeNode(inorder[start]);
        }

        for(int i=start; i <= stop; ++i) {
            if (inorder[i] == preorder[pre_index[0]]) {
                if (i == start) {
                    ++pre_index[0];
                    TreeNode right = buildTreeCore(preorder, inorder, pre_index, start+1, stop);
                    return new TreeNode(inorder[i], null, right);
                }
                else if (i == stop) {
                    ++pre_index[0];
                    TreeNode left = buildTreeCore(preorder, inorder, pre_index, start, stop-1);
                    return new TreeNode(inorder[i], left, null);
                }
                else {
                    ++pre_index[0];
                    TreeNode left = buildTreeCore(preorder, inorder, pre_index, start, i-1);
                    TreeNode right = buildTreeCore(preorder, inorder, pre_index, i+1, stop);
                    return new TreeNode(inorder[i], left, right);
                }
            }
        }

        return null;
    }
}