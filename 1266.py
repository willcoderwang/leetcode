class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(0, len(points) - 1):
            result += self.distance(points[i], points[i + 1])

        return result

    def distance(self, point1, point2):
        diff_x = abs(point1[0] - point2[0])
        diff_y = abs(point1[1] - point2[1])

        result = diff_x if diff_x >= diff_y else diff_y
        return result