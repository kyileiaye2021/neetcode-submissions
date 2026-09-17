import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        # heap queue
        # heapify the queue
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]

        # heap push the val to the heapq
        # we only need to store top k ele
        # in min heap, we have to pop out when the size exceeds k
        #   it will have kth largest num as the first ele


        
