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
        # check if the query point has its diagonal point
        for diag in self.point_freq:
            if abs(diag[0] - query[0]) != abs(diag[1] - query[1]) or diag[0] == query[0] or diag[1] == query[1]:
                continue

            print(f'Diagonal point to query point found: {diag}')
            # if the diagonal point to the query point exists
            diag_freq = self.point_freq[diag]
            print("diag_point freq", diag_freq)

            print(f"Other diagonal points: {(diag[0], query[1])} and {(query[0], diag[1])}")

            if (diag[0], query[1]) in self.point_freq and (query[0], diag[1]) in self.point_freq:
                print("other diagonal points found")
                count += (diag_freq * self.point_freq[(diag[0], query[1])] * self.point_freq[(query[0], diag[1])])
            else:
                count += 0
            print("num of squares made", count)
        return count