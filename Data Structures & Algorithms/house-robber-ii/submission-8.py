class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
            
        nums1 = nums[:len(nums) - 1] 
        nums2 = nums[1:]
        memo1 = [-1] * len(nums1)
        memo2 = [-1] * len(nums2)
        
        def helper(nums, memo):

            def recur_rob(i):
                if i >= len(nums):
                    return 0

                if memo[i] != -1:
                    return memo[i]

                memo[i] = max(recur_rob(i + 1), nums[i] + recur_rob(i + 2))

                return memo[i]
                
            return recur_rob(0)

        return max(helper(nums1, memo1), helper(nums2, memo2))

        
        

        