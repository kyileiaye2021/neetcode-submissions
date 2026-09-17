class CountSquares:

    def __init__(self):
        # hashmap {points: freq}
        self.point_freq = {}

    def add(self, point: List[int]) -> None:
        # must accept duplicate points
        point = tuple(point)
        self.point_freq[point] = 1 + self.point_freq.get(point, 0)

    def count(self, query: List[int]) -> int:
        # check if the point is forming a valid square with the three points 
        count = 0
        qx, qy = query
        # check if the query point has its diagonal point
        for dx, dy in self.point_freq:
            if abs(dx - qx) != abs(dy - qy) or dx == qx or dy == qy:
                continue

            # if the diagonal point to the query point exists
            diag_freq = self.point_freq[(dx, dy)]
            
            # find other diagonal points
            if (dx, qy) in self.point_freq and (qx, dy) in self.point_freq:
                count += (diag_freq * self.point_freq[(dx, qy)] * self.point_freq[(qx, dy)]) # num of squares we can make

            else:
                count += 0
            
        return count