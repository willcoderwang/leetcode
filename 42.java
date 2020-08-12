class Solution {
    public int trap(int[] height) {
        return trapCore(height, 0, height.length-1);
    }

    private int trapCore(int[] height, int start, int stop) {
        if (stop - start <= 1)
            return 0;

        int max = height[start];
        int max_index = start;
        for (int i=start+1; i <= stop; ++i) {
            if (height[i] > max) {
                max = height[i];
                max_index = i;
            }
        }

        if (max_index != start && max_index != stop) {
            return trapCore(height, start, max_index) + trapCore(height, max_index, stop);
        }

        else if (max_index == start) {
            int max2 = height[stop];
            int max2_index = stop;

            for (int i=stop; i > start; --i) {
                if(height[i] > max2) {
                    max2 = height[i];
                    max2_index = i;
                }
            }

            return trapBetweenMax(height, start, max2_index) + trapCore(height, max2_index, stop);
        }

        else {
            int max2 = height[start];
            int max2_index = start;

            for (int i=start+1; i < stop; ++i) {
                if(height[i] > max2) {
                    max2 = height[i];
                    max2_index = i;
                }
            }

            return trapBetweenMax(height, max2_index, stop) + trapCore(height, start, max2_index);
        }
    }

    private int trapBetweenMax(int[] height, int start, int stop) {
        int width = stop - start -1;
        int sum = 0;
        for (int i=start+1; i <stop; ++i) {
            sum += height[i];
        }

        return width * Math.min(height[start], height[stop]) - sum;
    }
}