class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # happy cases
        # [1,2,-3,4,5,-9]
        # [[1,2,-3], [4,5,-9]]

        # [1,2,-5,-2,1]
        # [[1,-2,1]]

        # edge cases
        # [1,2,-3,-3]
        # [[1,2,-3]]

        # [1,2,-3, 1,2,-3]
        # [[1,2,-3]]

        # [1,-1,0, 2,-2]
        # [[1,-1,0], [0,2,-2]]

        # [-1,0,1,2,-1,-4]
        # [[-1,-1,2],[-1,0,1]]

        # [0,0,0]
        # [[0,0,0]]

        # [1,2,-1]
        # []

        # iterate thru ele in the nums
        #   negate curr ith ele (target ele)
        #   create a hashmap
        #   iterate thru the ele with j from i + 1
        #       if curr target - jth ele in hashmap
        #           check if the [curr ith ele, ele in the hashmap, curr jth ele] not in the set
        #               add the list to the set
        #       else
        #           put curr jth ele to the hashmap
        # O(n^2) time
        
        # sort the ele
        # iterate thru the ele
        #   l and r
        #   negate curr ith ele (target)
        #   while l < r
        #       l and r pointer ele add upto target
        #           add the sublist triplet to res list
        #           l += 1
        #           while l ele = l - 1 ele
        #               l += 1
        #           while r ele = r - 1 ele
        #               r -= 1
        #        if l + r <target
        #           l += 1
        #           while l ele = l - 1 ele
        #               l += 1
        #       if l + r ele > target
        #           r -= 1
        #           while r ele. = r + 1 ele
        #           r -= 1
        #   return res list

        nums.sort()
        res = []

        i = 0
        while i < len(nums):

            target = - nums[i]

            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif nums[l] + nums[r] < target:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                else:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1

        return res
        







        