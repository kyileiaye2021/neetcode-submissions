class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # happy cases

        # Input: nums = [1,2,4,6]
        # Output: [48,24,12,8]

        # edge cases
#         Input: nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]

        # nums = [1, 2, 4, 6]
        # res = [1, 1, 2, 8] - forward pass
        # res = [48, 24, 12, 8] - backward pass
        # res = [48, 24, 12, 8]
        # res = [1,1,1,1] - initial

        forward_res = [1] * len(nums)
        backward_res = [1] * len(nums)
       
        for i in range(len(nums) - 1):

            forward_res[i + 1] = forward_res[i] * nums[i]

        for i in range(len(nums) - 1, 0, -1):
            backward_res[i - 1] = backward_res[i] * nums[i]

        for i in range(len(forward_res)):
            forward_res[i] = forward_res[i] * backward_res[i]

        return forward_res
           


        



