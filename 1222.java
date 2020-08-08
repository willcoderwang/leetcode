class Solution {
    public List<List<Integer>> queensAttacktheKing(int[][] queens, int[] king) {
        int[][] found_queens = new int[8][2];
        for (int[] f: found_queens) {
            f[0] = -1;
            f[1] = 1000;
        }

        for (int i=0; i < queens.length; ++i) {
            int[] q = queens[i];
            int d1 = q[0] - king[0];
            int d2 = q[1] - king[1];

            if (d1 == 0 || d2 == 0 || Math.abs(d1) == Math.abs(d2)) {
                int index = getIndex(d1, d2);
                if (index >= 0) {
                    if (found_queens[index][0] == -1 ||
                            (found_queens[index][0] != -1 &&
                                    found_queens[index][1] > Math.max(Math.abs(d1), Math.abs(d2)))) {
                        found_queens[index][0] = i;
                        found_queens[index][1] = Math.max(Math.abs(d1), Math.abs(d2));
                    }
                }
            }
        }

        List<List<Integer>> results = new ArrayList<List<Integer>>();
        for (int[] q: found_queens) {
            if (q[0] >= 0) {
                List<Integer> temp = new ArrayList<Integer>();
                temp.add(queens[q[0]][0]);
                temp.add(queens[q[0]][1]);
                results.add(temp);
            }
        }
        return results;
    }

    private int getIndex(int d1, int d2) {
        if (d1 == 0) {
            if (d2 == 0) {
                return -1;
            }
            else if (d2 > 0) {
                return 0;       // right
            }
            else {
                return 1;       // left
            }
        }
        else if (d1 > 0) {
            if (d2 == 0) {
                return 2;       // down
            }
            else if (d2 > 0) {
                return 3;       // down right
            }
            else {
                return 4;       // down left
            }
        }
        else {
            if (d2 == 0) {
                return 5;       // up
            }
            else if (d2 > 0) {
                return 6;       // up right
            }
            else {
                return 7;       // up left
            }
        }
    }
}