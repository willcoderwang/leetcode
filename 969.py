class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        results = []
        the_map = [0] * (len(arr)+1)
        for i, n in enumerate(arr):
            the_map[n] = i+1

        for i in range(len(arr), 0, -1):
            if the_map[i] == i:
                continue

            self.flip_2_last(arr, the_map, i, results)

        return results

    def flip_2_last(self, arr, the_map, i, results):
        if the_map[i] == 1:
            results.append(i)
            self.flip(arr, the_map, i)
        else:
            results.append(the_map[i])
            self.flip(arr, the_map, the_map[i])
            results.append(i)
            self.flip(arr, the_map, i)

    def flip(self, arr, the_map, n):
        for i in range(n//2):
            the_map[arr[i]] = n - 1 - i + 1
            the_map[arr[n - 1 - i]] = i + 1
            arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
