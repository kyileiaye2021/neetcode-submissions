class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # happy cases
        # input: points = [[0,2],[2,2]], k = 1
        # output: [0, 2]

        # input: points = [[0,2], [2,0],[2,2]], k = 2
        # output: [0, 2], [2,0]

        # edge cases
        # input: points = [[0,0]], k = 1
        # output: [0,0]

        # priority min heap
        
        # iterate thru the pairs
        #   calculate the dist between (0, 0) and curr pair
        #   add the pairs according to the dist

        # pop out the smallest dist and pairs for k times
        # append them to the res list
        # return res list
        min_heap = []
        res = []
        for (i, j) in points:
            dist = math.sqrt((j)**2 + (i)**2)
            heapq.heappush(min_heap, (dist, [i, j]))

        while k > 0:
            dist, pair = heapq.heappop(min_heap)
            res.append(pair)
            k -= 1
        return res

       