class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1

        results = [0] * n
        results[0] = 1
        for num in range(1, n):
            f_sqrt = math.sqrt(num+1)
            i_sqrt = int(f_sqrt)
            if math.pow(i_sqrt, 2) == num+1:
                results[num] = 1
                continue

            the_min = results[num-1] + 1
            i = 2
            while math.pow(i, 2) < num + 1:
                if results[int(num-math.pow(i, 2))] + 1 < the_min:
                    the_min = results[num-int(math.pow(i, 2))] + 1
                    if the_min == 2:
                        break

                i += 1

            results[num] = the_min

        return results[n-1]