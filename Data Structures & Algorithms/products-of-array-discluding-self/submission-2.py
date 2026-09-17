class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # O(n^2)

        # [1, 2,8, 48]
        # [48,48,24,6]

        # first create left arr and right arr
        # iterate thru the list
        #   for the ith position
        #   multiply the ele before the ith pos and after pos
        
        # return the lst

        left_multiply = [1] * len(nums)
        right_multiply = [1] * len(nums)
        res = []
        
        left_multiply[0] = nums[0]
        for i in range(1, len(nums)):

            left_multiply[i] = nums[i] * left_multiply[i - 1] 
        print(left_multiply)

        right_multiply[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            right_multiply[i] = nums[i] * right_multiply[i + 1]
        print(right_multiply)

        for i in range(len(nums)):
            if i == 0:
                nums[i] = right_multiply[i+1]
            elif i == len(nums) - 1:
                nums[i] = left_multiply[i - 1]
            else:
                nums[i] = left_multiply[i - 1] * right_multiply[i + 1]

        return nums
            

            


        