import heapq


class MedianFinder:

    def __init__(self):
        self.smaller_half = []
        self.bigger_half = []

    def addNum(self, num: int) -> None:
        if len(self.smaller_half) <= len(self.bigger_half):
            if self.bigger_half and num > self.bigger_half[0]:
                num = heapq.heapreplace(self.bigger_half, num)

            heapq.heappush(self.smaller_half, -num)
        else:
            if num < -self.smaller_half[0]:
                num = -heapq.heapreplace(self.smaller_half, -num)

            heapq.heappush(self.bigger_half, num)

    def findMedian(self) -> float:
        print(self.smaller_half)
        print(self.bigger_half)
        if len(self.smaller_half) == len(self.bigger_half):
            return (-self.smaller_half[0] + self.bigger_half[0]) / 2
        else:
            return -self.smaller_half[0]

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
param_2 = obj.findMedian()
print(param_2)