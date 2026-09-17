class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp array first all initialized to 1
        # prevMin , prevMax = 1, 1

        # iterate thru the list
        # curr max =  max(prevMin * curr num , prevMax * curr num, curr num)
        # curr min = min(prevMin * curr num , prevMax * curr num, curr num)
        # put it in the dp array at curr position

        # return the max of the two min and max value at the last dp slot

        dp = [[1, 1]] * (len(nums) + 1)

        for i, ele in enumerate(nums):
            curr_max = max(ele, dp[i][0] * ele, dp[i][1] * ele)
            curr_min = min(ele, dp[i][0] * ele, dp[i][1] * ele)

            dp[i + 1] = [curr_max, curr_min]

        res = float('-inf')
        for i in range(1, len(dp)):
            if dp[i][0] > res:
                res = dp[i][0]
        
        return res

