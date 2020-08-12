class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<>();

        if (numRows < 1) {
            return result;
        }

        List<Integer> list1 = new ArrayList<>();
        list1.add(1);
        result.add(list1);

        for (int n=1; n < numRows; ++n) {
            List<Integer> last_line = result.get(result.size()-1);
            List<Integer> new_last_line = new ArrayList<>();
            new_last_line.add(1);

            for(int i=0; i < last_line.size()-1; ++i) {
                new_last_line.add(last_line.get(i) + last_line.get(i+1));
            }

            new_last_line.add(1);
            result.add(new_last_line);
        }

        return result;
    }
}