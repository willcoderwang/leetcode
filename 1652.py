class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)

        ak = abs(k)
        s = sum(code[:ak])
        result = []
        for i in range(len(code)):
            if i+ak < len(code):
                r = s - code[i] + code[i+ak]
            else:
                r = s - code[i] + code[i+ak-len(code)]

            s = r
            result.append(s)

        if k < 0:
            result = self.rotate(result, ak+1)

        return result

    def rotate(self, a_list, r):
        first_part = a_list[:-r]
        second_part = a_list[len(a_list)-r:]
        return second_part + first_part
