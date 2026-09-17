class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # input: [5,5,1,1,1,5,5]
        # output: 5

        # input: [1,2,2,3,3,3]
        # output: 3

        # input: [2,1,2]
        # output: 2

        # input: []
        # output: None

        # input: [2]
        # output: 2

        # input: [1,1,1]
        # output: 1

        # hashmap
        # time - O(n)
        # space - O(n)

        # map = collections.defaultdict(int)
        # for n in nums:
        #     map[n] = map.get(n, 0) + 1

        # max_val = float('-inf')
        # maj_ele = ""
        # for key, val in map.items():
        #     if val > max_val:
        #         max_val = max(val, max_val)
        #         maj_ele = key

        # return maj_ele

        res = nums[0]
        count = 0

        for n in nums:
            if count == 0:
                res = n

            if res == n:
                count += 1
            else:
                count -= 1

        return res







  