class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if self.with_even_digits(num):
                count += 1

        return count

    def with_even_digits(self, num):
        while not 0 <= num <= 9 and not 10 <= num <= 99:
            num //= 100

        if 10 <= num <= 99:
            return True

        return False