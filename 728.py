class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right + 1):
            if self.is_dividing_number(num):
                res.append(num)

        return res

    @staticmethod
    def is_dividing_number(num):
        if num == 0:
            return False

        num_copy = num

        while num:
            i = num % 10
            if i == 0 or num_copy % i != 0:
                return False

            num /= 10
            num = int(num)

        return True