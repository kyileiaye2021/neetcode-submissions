class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # [2,2,3,5,6], k = 5
        # [2,3,4,5,6],k =4
        # [3,4,4,5,6], k = 3
        # [4,4,5,6,6], k = 2
        # [4,5,6,6,8], k = 1
        
        # (1,1), (2,0), (3,2), (5,3), (6,4)
        # [(2,0), (2,1), (3,2), (5,3), (6,4)]

        # [(1,0),(2,1)], k = 3
        # [(2,1), (4, 0)] k = 2
        # [(4, 0), (8, 1)], k = 1
        # [(8, 1), (16, 0)], k = 0

        # res = nums[:]
        min_heap = []
        for i in range(len(nums)):
            min_heap.append((nums[i], i)) 

        heapq.heapify(min_heap)

        for _ in range(k):
            ele, index = heapq.heappop(min_heap) 
            print(f"index: {index}")
            # res[index] *= multiplier
            heapq.heappush(min_heap, (ele * multiplier, index))

        res = [0] * len(nums)
        for ele, index in min_heap:
            res[index] = ele

        return res


        

        
