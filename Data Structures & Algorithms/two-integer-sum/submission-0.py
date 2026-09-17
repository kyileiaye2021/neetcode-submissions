class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dict
        # iterate over the ele in the list
        #   difference between the target and curr val
        #   check if the diff is in the dict
        #       return a list of indices of difference and curr ele
        #   add the curr ele with its index to the dict 

        index_dict = {}

        for i, ele in enumerate(nums):
            dif = target - ele

            if dif in index_dict:
                return [index_dict[dif], i]

            else:
                index_dict[ele] = i