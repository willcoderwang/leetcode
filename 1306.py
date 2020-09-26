class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        the_hash = [None] * len(arr)

        while True:
            changed = False
            for i, v in enumerate(arr):
                if the_hash[i] is not None:
                    continue

                if i + arr[i] < len(arr) and (arr[i+arr[i]] == 0 or the_hash[i+arr[i]]):
                    the_hash[i] = True
                    changed = True
                    if start == i:
                        return True

                if i - arr[i] >= 0 and (arr[i-arr[i]] == 0 or the_hash[i-arr[i]]):
                    the_hash[i] = True
                    changed = True
                    if start == i:
                        return True

            if not changed:
                return False
