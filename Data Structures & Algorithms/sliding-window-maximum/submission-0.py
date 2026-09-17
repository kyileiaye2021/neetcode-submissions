class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # happy case
        # Input: nums = [1,2,1,0,4,2,6], k = 3
        # Output: [2,2,4,4,6]

        # input: nums = [1,2,3,4], k = 2
        # output: [2,4]

        # input: nums = [1,5,1], k = 2
        # output: [5, 5]

        # edge case
        # input: nums = [1], k = 1
        # output: [1]
        
        # input; nums = [], k = 0
        # output: [0]

        # sliding window
        # res list
        #l =0 , r = l + k - 1
        # until r reaches the end of the nums
        #   biggest = l ele
        #   iterate thru l to r
        #       get the biggest ele 
        #   append the biggest ele to the res
        #   l moved by 1
        #   r moved by 1

        res = []
        l = 0
        r = l + k - 1
        while r < len(nums):
            biggest = nums[l]
            for i in range(l, r + 1):
                if nums[i] > biggest:
                    biggest = nums[i]
            res.append(biggest)

            l += 1
            r += 1

        return res


