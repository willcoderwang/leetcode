class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = [0, 0, 0]
        for b in bills:
            if b == 5:
                changes[0] += 1
            elif b == 10:
                changes[1] += 1
                changes[0] -= 1
            elif b == 20:
                changes[2] += 1
                if changes[1] > 0:
                    changes[1] -= 1
                    changes[0] -= 1
                else:
                    changes[0] -= 3

            if changes[0] < 0 or changes[1] < 0 or changes[2] < 0:
                return False

        return True