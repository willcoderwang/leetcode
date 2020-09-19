class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        the_map = [[False for i in range(60)] for j in range(24)]

        for tp in timePoints:
            hour = int(tp[:2])
            minute = int(tp[3:])
            if the_map[hour][minute]:
                return 0

            the_map[hour][minute] = True

        first_hour, first_minute = None, None
        pre_hour, pre_minute = None, None
        the_min = 1440  # 24 * 60

        for h in range(24):
            for m in range(60):
                if the_map[h][m]:
                    if first_hour is None:
                        first_hour, first_minute = h, m
                        pre_hour, pre_minute = h, m
                        continue
                    else:
                        temp = (h - pre_hour) * 60 + (m - pre_minute)
                        the_min = min(the_min, temp)
                        pre_hour, pre_minute = h, m

        temp = 1440 - ((pre_hour - first_hour) * 60 + (pre_minute - first_minute))

        return min(temp, the_min)
