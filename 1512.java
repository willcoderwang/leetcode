class Solution {
    public int numIdenticalPairs(int[] nums) {
        int[] arr = new int[100];

        for (int num: nums) {
            arr[num-1] += 1;
        }

        int sum = 0;
        for (int n: arr) {
            sum += n * (n - 1) / 2;
        }

        return sum;
    }
}