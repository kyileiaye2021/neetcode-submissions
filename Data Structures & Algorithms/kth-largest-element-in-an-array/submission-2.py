class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # max heap
        pq = []

        for n in nums:
            heapq.heappush(pq, -n)

        # [-5,-4,-3,-2,-1]
        res = 0
        while k > 0:
            res = heapq.heappop(pq)
            k -= 1

        return -res
