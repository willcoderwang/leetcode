class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        the_map = [[None for i in range(T+1)] for j in range(T+1)]
        return self.least_clips(clips, the_map, 0, T)

    def least_clips(self, clips, the_map, start, stop):
        if stop < start:
            return 0

        temp_min = -1

        for c in clips:
            if the_map[start][stop] is not None:
                return the_map[start][stop]

            if c[0] <= start and c[1] >= stop:
                the_map[start][stop] = 1
                return 1
            elif c[0] > stop or c[1] < start or c[1] <= c[0]:
                continue
            elif c[0] <= start < c[1]:
                left_res = self.least_clips(clips, the_map, c[1], stop)
                if left_res < 0:
                    continue

                if temp_min < 0:
                    temp_min = 1 + left_res
                else:
                    temp_min = min(temp_min, 1 + left_res)
            elif c[0] < stop <= c[1]:
                left_res = self.least_clips(clips, the_map, start, c[0])
                if left_res < 0:
                    continue

                if temp_min < 0:
                    temp_min = 1 + left_res
                else:
                    temp_min = min(temp_min, 1 + left_res)
            elif c[0] >= start and c[1] <= stop:
                left_res_l = self.least_clips(clips, the_map, start, c[0])
                left_res_r = self.least_clips(clips, the_map, c[1]+1, stop)

                if left_res_l < 0 or left_res_r < 0:
                    continue

                if temp_min < 0:
                    temp_min = 1 + left_res_l + left_res_r
                else:
                    temp_min = min(temp_min, 1 + left_res_l + left_res_r)

        the_map[start][stop] = temp_min

        return temp_min
