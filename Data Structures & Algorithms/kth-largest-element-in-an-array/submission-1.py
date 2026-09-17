class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap
        # heapify the arr
        # remove all ele except for k ele
        # return the first ele

        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]