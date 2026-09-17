class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [1,2,3,4], k = 2
        # [1,2,3,4]
        
        # [2,2,2,2], k = 2
        # [2]

        # [2,2,2,3,3], k = 2
        # [2,3]

        # [1,7,7,7], k = 2
        # [1,7]

        # [1,7,7], k = 1
        # [7]

        # [], k = 0
        # []

        # hashmap
        freq = Counter(nums)
        temp = [[] for i in range(len(nums) + 1)]
        res = []

        # sort the hashmap based on the values nlog(n)
        # create an arr 
        # the arr index would be freq
        # based on the freq, the vals will be  assigned to the position of that freq index

        for key, val in freq.items():
            temp[val].append(key)

        for i in range(len(temp) - 1, 0, -1):
            for ele in temp[i]:
                res.append(ele)

            if len(res) == k:
                return res



    