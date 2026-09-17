class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums = [-1, 0, 1, 2, -1,-4]
        # [-4,-1,-1, 0, 1, 2]
        # 
        # iterate thru the ele
        #   skip if the ith ele is the same as i + 1 th ele
        #   l = i + 1
        #   r = len(nums) - 1
        #   while l != r
        #       sum = nums[l] + nums[r]
        #       if sum + ith ele > 0
        #           decrement r by 1
        #       elif sum + ith ele < 0
        #           increment l by 1
        #       else
        #           return [ith ele, nums[l], nums[r]]

        # [-4,-1,-1, 0, 1, 2]
        
        res = []
        # if len(nums) == 3:
        #     return nums if sum(nums) == 0 else res

        nums.sort()
        for i in range(len(nums)):
                curr = nums[i]
                if i > 0 and curr == nums[i - 1]:
                    continue

                l = i + 1
                r = len(nums) - 1
                while l < r:
                    if curr + nums[l] + nums[r] > 0:
                        r -= 1

                    elif curr + nums[l] + nums[r] < 0:
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                    else:
                        res.append([curr, nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
        return res


