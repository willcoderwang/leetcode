class Solution:
    def numberOfBoomerangs(self, points) -> int:
        if len(points) < 3:
            return 0

        the_map = [[0 for _ in range(len(points))] for _ in range(len(points))]

        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                dist = self.distance_square(points[i], points[j])
                the_map[i][j] = dist
                the_map[j][i] = dist

        result = 0
        for p in range(len(points)):
            the_dict = dict()
            for d in the_map[p]:
                if d <= 0:
                    continue
                if d not in the_dict:
                    the_dict[d] = 1
                else:
                    the_dict[d] += 1

            for k, v in the_dict.items():
                result += (v * (v-1))

        return result

    def distance_square(self, point1, point2):
        return (point1[0] - point2[0]) * (point1[0] - point2[0]) + (point1[1] - point2[1]) * (point1[1] - point2[1])
