class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # input: [2,3,4,5], target = 9
        # output: [2,3]

        # input: [1,1, 2], target = 2
        # output: [0,1]

        # input: [3,7], target = 10
        # output: [0,1]

        # Binary search technique/ two pointer technique
        # this only works if the array is sorted

        # i, j = 0, len(nums) - 1

        # while i < j:
            
        #     sum = nums[i] + nums[j]

        #     if sum < target:
        #         i += 1

        #     elif sum > target:
        #         j -= 1
            
        #     else:
        #         return [i, j]

        # two pointer 
        # hash map

        map = {} # {val: index}

        for i, ele in enumerate(nums):
            diff = target - ele

            if diff in map:
                return [map[diff], i]

            else:
                map[ele] = i



        
            