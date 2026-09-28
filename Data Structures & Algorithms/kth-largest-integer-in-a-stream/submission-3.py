class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # min heap
        # add the ele in the min heap
        # if max heap size > k
        #   pop the min ele

        # O(nlogk)
        self.min_heap = []
        self.k = k
        for n in nums:
            heapq.heappush(self.min_heap, n)
            if len(self.min_heap) > k:
                heapq.heappop(self.min_heap)


    def add(self, val: int) -> int:
        # add the ele in the min heap
        # if max heap size > k
        #   pop the min ele
        # return first ele

        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)

        return self.min_heap[0]


        
