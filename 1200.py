class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = 2 * 10 ^ 6 + 1
        results = []
        for index in range(len(arr)-1):
            diff = arr[index+1] - arr[index]
            if diff < min_diff:
                min_diff = diff
                results = [[arr[index], arr[index+1]]]
            elif diff == min_diff:
                results.append([arr[index], arr[index+1]])

        return results