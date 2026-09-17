class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the ele first
        # iterate thru the list
        #   two pointer approach to find the two ele
        #   left =  curr + 1
        #   right = end of the list
        #   find the sum of the three that add up to 0
        #   add the list to res

        nums.sort()

        res = []
        i = 1
        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[j] + nums[k] + nums[i] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

                elif nums[j] + nums[k] + nums[i] < 0:
                    j += 1

                else:
                    k -= 1

        return list(res)


