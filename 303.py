class NumArray:
    sum_left = None

    def __init__(self, nums: List[int]):
        self.sum_left = []
        tmp_sum = 0
        for n in nums:
            tmp_sum += n
            self.sum_left.append(tmp_sum)

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            left_sum = self.sum_left[left - 1]
        else:
            left_sum = 0

        return self.sum_left[right] - left_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)