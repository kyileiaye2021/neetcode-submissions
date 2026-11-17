class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # happy cases
        # nums = [-1,0,1]
        # output = [-1,0,1]

        # nums = [-1,0,1,2,-2]
        # output = [[-1,0,1], [-2,0,2]]

        # nums = [0,0,0]
        # output = [[0,0,0]]

        # edge cases
        # nums = [-1,0,1,1,-1]
        # output = [-1,0,1]

        # nums = [2,1,4]
        # output = []

        # nums = [0]
        # output = []

        # hashmap (not sorted)
        # res
        # iterate thru the ele
        #   target = -curr ele
        #   create a set
        #   iterate thru the other ele
        #       check if the diff (target - curr ele) in set
        #           just create a list triplet, sort it, and add it to the res
        #       add the curr ele to the set
        #       

        # two pointer (sort)
        # sort the nums
        # iterate thru the ele
        #   if i > 0 and i ele == i - 1 ele
        #       continue
        #   l = i + 1
        #   r = len(nums) - 1
        #   while l < r
        #       total = curr ith ele + l ele + r ele
        #       check if total = 0
        #           add it to the res
        #           l += 1
        #           r -= 1
        #           there can be duplicates as well here; need to skip
        #       if total > 0
        #           r -= 1
        #           if r ele == r + 1 ele
        #               r -= 1
        #       else
        #           l += 1
        #           if l ele == l - 1 ele
        #               l += 1

        nums.sort()
        res = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                elif total > 0:
                    r -= 1

                else:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res





