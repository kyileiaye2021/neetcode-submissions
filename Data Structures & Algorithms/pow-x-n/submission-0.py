class Solution:
    def myPow(self, x: float, n: int) -> float:

        # whilie n > 0:
        #   multiply x to res and update the res
        res = 1
        temp = n

        if n == 0:
            return res
            
        if n < 0:
            n = n * (-1)

        while n > 0:
            res *= x
            n -= 1

        return res if temp > 0 else (1 / res)

        