class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # happy case 
        # [1,2,3]
        # 6

        # [-1,-2,-3]
        # 6

        # curr min and max
        # itereate thru the ele
        #   if curr min or max becomes 0
        #       reset curr min and curr max = 1

        #   curr min = min(n * currmin , n * currmax, n) [-1, 8]
        #   curr max = max(n * currmin , n * currmax, n)
        #   res = max(curr_min, curr_max)
        # return res


        currMin, currMax = 1, 1
        res = max(nums)

        for n in nums:

            if n == 0:
                currMin, currMax = 1, 1

            temp = currMin
            currMin = min(n * currMax, n * currMin, n)
            currMax = max(n * currMax, n * temp, n)
            res = max(currMin, currMax, res)

        return res


        