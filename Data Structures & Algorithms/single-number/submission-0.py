class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # freq map (O(n) time and O(n) space)
        
        # set (O(n) time and O(n) space)
        
        # using XOR operations
        
        # 6^6 = 0
        # 6^6^6= 0
        # 2^4^4^2 = 0
        # 2^4^6^4^2 = 6

        # 0^n = n

        # nums = [2]
        # output: 2

        # nums = [4,4]
        # output: 0

        

        res = 0

        for n in nums:
            res = res ^ n

        return res