class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min heap 
        # k largest dist will be left in the heap

        smallest_dist = [] # (pair, [x, y])

        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(smallest_dist, (-dist, [x, y]))
            while len(smallest_dist) > k:
                heapq.heappop(smallest_dist)

        return [[x,y] for dist, [x,y] in smallest_dist]