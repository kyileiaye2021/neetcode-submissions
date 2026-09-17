class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create a dict
        freq_dict = {}

        # populate the dict
        for ele in nums:
            freq_dict[ele] = 1 + freq_dict.get(ele, 0)

        # create a bucket the same size with the input array
        # the largest count can be the size of the input array
        count_bucket = [[] for i in range(len(nums) + 1)]

        # insert the ele in the bucket based on their freq
        for ele, count in freq_dict.items():
            count_bucket[count].append(ele)

        # getting top k freq ele
        res = []
        for i in range(len(count_bucket) - 1, 0, -1):
            for ele in count_bucket[i]:
                res.append(ele)
                if len(res) == k:
                    return res


