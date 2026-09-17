class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # happy cases
        # input - [1,-1,0]
        # output - [[1,-1,0]]

        # edge case
        # input - [1,1,0]
        # output - []

        # input - [0,0,0]
        # output - [[0,0,0]]

        # Brute force 
        # create a res list
        # sort the arr (nlogn)
        # iterate the sorted arr (n)
        #   l,r
        #   target = - curr ele
        #   while l < r (n/2)
        #       check if the sum of l and r ele is the same as target
        #       create a list of l,r,i ele
        #       if the list is not already in the res list
        #           add it to the res list
        # return res list

        res = []
        nums = sorted(nums)

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            target = 0 - nums[i] # nums[l] + nums[r]

            while l < r:
                sum = nums[l] + nums[r]
                if sum == target:
                    cur_lst = [nums[i], nums[l], nums[r]]
                    if cur_lst not in res:
                        res.append(cur_lst)

                    l += 1
                    r -= 1

                elif sum > target:
                    r -= 1

                else:
                    l += 1

        return res

                


