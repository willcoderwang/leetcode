class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target < letters[0] or target >= letters[-1]:
            return letters[0]

        start = 0
        end = len(letters) - 1
        while start < end:
            mid = (end + start) // 2
            if letters[mid] <= target < letters[mid + 1]:
                return letters[mid + 1]
            elif letters[mid + 1] <= target:
                start = mid + 1
            else:
                end = mid

        return letters[start + 1]