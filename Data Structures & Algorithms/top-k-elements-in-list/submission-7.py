class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [1,2,2,3,3,3], k = 2
        # output: [2, 3]

        # nums = [7,7], k = 1
        # output: 1

        # nums = [4, 2, 7, 7], k = 1
        # output: [7]

        # nums = [-9, 0, 7, 7, 8, 8], k = 2
        # output: [7, 8]

        # hashmap (nlogn)
        # heap (nlogk)
        # bucket sort (n)

        # freq count
        freq = Counter(nums)
        largest_count = max(freq.values())

        # craete the arr of largest freq count
        temp = [[] for _ in range(largest_count + 1)]

        for key, val in freq.items():
            temp[val].append(key)
        
        print(temp)
        res = []
        for i in range(len(temp) - 1, 0, -1):
            for val in temp[i]:
                if temp[i] == 0:
                    continue

                res.append(val)
                if len(res) == k:
                    return res

            

        # iterate thru the ele from the last down to 1
        #   skip the ele if the ele is 0
        #   otherwise, add the ele to the arr
        #   if the res contains k ele
        #       return res






