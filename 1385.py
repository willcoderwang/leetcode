class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        result = 0
        for num1 in arr1:
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    break
            else:
                result += 1

        return result