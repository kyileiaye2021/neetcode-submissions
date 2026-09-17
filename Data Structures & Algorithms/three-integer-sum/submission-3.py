class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # happy cases
        # input: nums = [-1,0, 1, 2, -1, -4]
        # sorted = [-4, -1, -1, 0, 1, 2]
        # output: [[-1, -1, 2], [-1, 0, 1]]

        # edge cases
        # input: nums = [-1, 2, 2]
        # output: []

        # input: nums = [0, 0, 0]
        # output: [[0, 0, 0]]

        # Brute force O(n^3)
        # Two pointer --> O(n^2) time, O(n) space 
        # sorted, two pointer binary search approach --> O(n^2), O(1) space

        nums.sort()
        res = []

        for i, n in enumerate(nums):

            # # skip duplicates
            # if i > 0 and nums[i] == nums[i -1]:
            #     continue

            l, r = i + 1, len(nums) - 1

            while l < r:

                sum = n + nums[l] + nums[r]

                if sum > 0:
                    r -= 1

                elif sum < 0:
                    l += 1

                else:
                    curr_res = [n, nums[l], nums[r]]
                    if curr_res not in res:
                        res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # while nums[l] == nums[l - 1] and l < r:
                    #     l += 1

        return res
                
            

