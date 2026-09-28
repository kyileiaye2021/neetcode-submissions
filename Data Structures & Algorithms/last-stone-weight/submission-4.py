class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap
        # heapify stones
        # pop out until there is one stone
        #   pop out 2 stones
        #   if 2 stones != ; x - y and add res to max heap
        # return ele in max heap

        max_heap = []
        for s in stones:
            heapq.heappush(max_heap, -s)

        while len(max_heap) > 1:
            if max_heap:
                first = -heapq.heappop(max_heap)
                second = -heapq.heappop(max_heap)
                res = first - second if first > second else second - first
                if res != 0:
                    heapq.heappush(max_heap, -res)

        return -max_heap[0] if max_heap else 0
