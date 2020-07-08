class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]

        result = [-1]
        the_min = arr[-1]
        for n in reversed(arr[:-1]):
            result.append(the_min)
            if n > the_min:
                the_min = n

        result.reverse()
        return result