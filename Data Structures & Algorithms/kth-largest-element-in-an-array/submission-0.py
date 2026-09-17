class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap
        # create min heap nums
        # pop the min ele until the len of min heap is equal to k
        # return the first ele in the min heap

        min_heap = nums
        heapq.heapify(min_heap) # O(n)
        while len(min_heap) > k: # popping out n-k times
            heapq.heappop(min_heap) # O(log(n))

        return min_heap[0]


        # time complexity - O(n) + O(n-k * O(logn))
        # space complexity - O(n)