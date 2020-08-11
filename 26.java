class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length <= 1)
            return nums.length;

        int len = 1;
        int toBeReplaced = 1;
        int previousValue = nums[0];

        for (int i=1; i<nums.length; ++i) {
            if (nums[i] != previousValue) {
                nums[toBeReplaced] = nums[i];
                ++toBeReplaced;
                ++len;
                previousValue = nums[i];
            }
        }

        return len;
    }
}