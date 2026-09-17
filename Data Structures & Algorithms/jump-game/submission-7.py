class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # at every index, we jump

        # i = 0
        # while i < last index
        #   if curr ith ele = 0: 
        #       return False
        #   add the curr ith ele to i
        # return True

        # i = 0
        # last = len(nums) - 1

        # while i < last:
        #     if nums[i] == 0:
        #         return False

        #     i += nums[i]

        # return True

        # from the curr position, how far we can reach
        # iterate thru the ele
        #   add the ele to its corresponding index
        #   append the next index we will reach

        # iterate thru the index arr
        #   get the largest index
        # return true if the largest index >= last

        # idx_arr = []
        # for i in range(len(nums) - 1):
        #     index = i + nums[i]
        #     idx_arr.append(index)

        # if len(idx_arr) == 0:
        #     return True

        # largest = idx_arr[0]
        # for idx in idx_arr:
        #     largest = max(largest, idx)

        # return True if largest >= len(nums) - 1 else False

        # starting from the end, check if the prev can reach to the end
        #   if it does
        #       move the des to the prev
        #   move to prev to prev -1
        
        # if the goal is equal to 0
        #   return true

        last = len(nums) - 1
        start = 0
       
        for i in range(last - 1, start - 1, -1):
            
            if i + nums[i] >= last:
                last = i


        return True if last == start else False
