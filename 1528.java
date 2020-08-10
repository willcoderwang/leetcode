class Solution {
    public String restoreString(String s, int[] indices) {
        char[] charArr = s.toCharArray();
        quickSort(charArr, indices, 0, indices.length-1);
        return new String(charArr);
    }

    private void quickSort(char[] s, int[] indices, int start, int stop) {
        if (start >= stop)
            return;

        int front = start;
        int end = stop;

        while (front < end) {
            while (front < end) {
                if (indices[end] < indices[front]) {
                    int temp = indices[end];
                    indices[end] = indices[front];
                    indices[front] = temp;

                    char temp_c = s[end];
                    s[end] = s[front];
                    s[front] = temp_c;

                    break;
                }

                --end;
            }

            while (front < end) {
                if (indices[end] < indices[front]) {
                    int temp = indices[end];
                    indices[end] = indices[front];
                    indices[front] = temp;

                    char temp_c = s[end];
                    s[end] = s[front];
                    s[front] = temp_c;

                    break;
                }

                ++front;
            }
        }

        quickSort(s, indices, start, front-1);
        quickSort(s, indices, front+1, stop);
    }
}