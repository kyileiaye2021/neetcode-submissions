class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # hashmap

        freq_map = {}

        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1

        res_lst = [[] for i in range(len(nums) + 1)]
        
        for ele, freq in freq_map.items():
            res_lst[freq].append(ele)

        res = []
        for i in range(len(res_lst) - 1, 0, -1):
            for ele in res_lst[i]:
                res.append(ele)
                k -= 1
                if k == 0:
                    return res
        