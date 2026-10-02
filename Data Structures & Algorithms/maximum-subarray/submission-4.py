class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # two pointer sliding window
        total = 0
        res = float('-inf')
        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        
        return res
