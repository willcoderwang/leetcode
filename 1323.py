class Solution:
    def maximum69Number (self, num: int) -> int:
        if num // 1000 % 10 == 6:
            return num + 3000
        elif num // 100 % 10 == 6:
            return num + 300
        elif num // 10 % 10 == 6:
            return num + 30
        elif num // 1 % 10 == 6:
            return num + 3
        else:
            return num