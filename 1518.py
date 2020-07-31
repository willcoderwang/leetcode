class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        left_bottles = 0
        new_bottles = numBottles
        total = new_bottles

        while left_bottles + new_bottles >= numExchange:
            next_new_bottles = (left_bottles + new_bottles) // numExchange
            next_left_bottles = (left_bottles + new_bottles) % numExchange
            new_bottles = next_new_bottles
            left_bottles = next_left_bottles
            total += new_bottles

        return total