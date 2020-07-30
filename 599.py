class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = None
        res_sum = 2001

        for index1, r1 in enumerate(list1):
            for index2, r2 in enumerate(list2):
                if r1 == r2:
                    if res_sum > index1 + index2:
                        res = [r1]
                        res_sum = index1 + index2
                    elif res_sum == index1 + index2:
                        res.append(r1)

        return res