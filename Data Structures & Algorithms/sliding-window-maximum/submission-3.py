class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # dq = {}
        # l, r = 0, 0 
        # res = []
        # iterate thru the ele with r 
        #   while last ele of dq > curr ele
        #       remove that last ele 
        #   add the curr ele
        #   
        #.  if first index of dq < l:
        #       pop the first index

        #   if r - l + 1 >= k: 
        #       add the leftmost ele of dq to res
        #       l += 1

        # return res

        # dq = deque()
        # l = 0
        # r = 0
        # res = []

        # while r < len(nums):
        #     while dq and nums[dq[-1]] < nums[r]:
        #         dq.pop()
        #     dq.append(r)

        #     if l > dq[0]:
        #         dq.popleft()

        #     if  r - l + 1 >= k:
        #         res.append(nums[dq[0]])
        #         l += 1
            

        #     r += 1

        # return res

        heap = []
        l = 0
        r = 0
        res = []

        while r < len(nums):
            heapq.heappush(heap, (-nums[r], r))
            while heap and heap[0][1] < l:
                heapq.heappop(heap)

            if r - l + 1 >= k:
                res.append(-heap[0][0])
                l += 1
            

            r += 1
        return res



