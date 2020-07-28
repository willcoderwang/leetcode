class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target_cp = target.copy()
        arr_cp = arr.copy()
        target_cp.sort()
        arr_cp.sort()
        return target_cp == arr_cp