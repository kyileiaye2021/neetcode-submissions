class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # [1,2]
        # [[1,2], [2,1]]

        # [1]
        # [[1]]

        # []
        # [[]]

        # [1,2] 
        # [2] -> add the curr ith num to the res at every i point
        # [] -> append it to the res and return/backtrack

        
        # base case
        if len(nums) == 0:
            return [[]]
        # going to the depth until all elements are gone
        permute_arr = self.permute(nums[1:])

        res = []
        for p in permute_arr:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res


