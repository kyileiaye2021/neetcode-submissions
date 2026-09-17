class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # happy cases

        # Input: stones = [2,3,6,2,4]
        # [2,2,3,4,6]
        # [2,2,2,3]
        # [1,2,2]
        # [1]

        # edge cases
        # input: stones = [1,2]
        # output: 1

        # input: stones = [1,1]
        # output: 0

        # input: stones = [1]
        # output: 1

        # maxHeap
        # negate all elements in the list 
        # until len of maxHeap = 1
        #   pop out the two ele 
        #   compare the two ele, x, y
        #   if x > y
        #       heappush x-y to the maxheap
        #   elif x < y
        #       heappush y-x to maxheap
        # return maxHeap[0]

        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)


        if len(max_heap) == 1:
            return stones[0]

        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, y - x)

        return (- max_heap[0])
