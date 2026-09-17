class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # happy cases
        # nums = [1,2,2,3,3,3], k = 2
        # [3, 2]

        # nums = [2,3,3], k = 2
        # [2,3]

        # edge cases
        # nums = [1,1,1], k = 1
        # [1]

        # nums = [], k = 1
        # []

        # hashmap 
        # {1:1, 2:2, 3:3}
        # max heap
        # [(3,3), (2,2), (1,1)]
        # pop from max heap k times and append the popped ele to res list# O(k log n)

        nums_hashmap = Counter(nums)
        max_heap = []

        for key, val in nums_hashmap.items():
            heapq.heappush(max_heap, (-val, key))

        res_lst = []
        for i in range(k):
            val, key = heapq.heappop(max_heap)
            res_lst.append(key)

        return res_lst



