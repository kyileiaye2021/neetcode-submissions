class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # happy case
        # points = [[0,2],[2,2]], k = 1
        # output: [[0,2]]

        # points = [[0,2]], k = 1
        # output: [[0,2]]

        # points = [[0, 2], [2, 0]], k = 2
        # output: [[0,2],[2,0]]

        # points = [[0,0]], k = 1
        # output: [[0,0]]

        # a hashmap {dist: [x,y]}
        # iterate thru the ele
        #   calculate the distance
        #   add the dist to curr [x, y]

        # sort the dist hashmap based on the dist key
        # get the k key-val pairs
        # return the val lists 

        # min_heap 
        # iterate thru the pairs
        #   calculate the dist
        #   store the dist into the list along with the pairs

        # while len of max heap > k
        #   pop out the pairs 

        min_heap = []
        for x, y in points:
            dist = (x ** 2) + (y **2)
            min_heap.append([dist, x, y])

        heapq.heapify(min_heap)

        res = []
        while k > 0:
            dist, x, y = heapq.heappop(min_heap)
            res.append([x, y])
            k -= 1

        return res



