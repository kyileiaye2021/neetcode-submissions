class Solution:
    def rev(self, x, n):
        # base case
        if n == 0:
            return 1

        if x == 0:
            return 0

        res = self.rev(x, n // 2)
        res *= res
        return res if n % 2 == 0 else (res * x)

    def myPow(self, x: float, n: int) -> float:

        # # whilie n > 0:
        # #   multiply x to res and update the res

        # # O(n) time and O(1) space
        # res = 1
        # temp = n

        # if n == 0:
        #     return res

        # if n < 0:
        #     n = n * (-1)

        # while n > 0:
        #     res *= x
        #     n -= 1

        # return res if temp > 0 else (1 / res)

        # divide and conquer
        # O(log n)
        # O(logn) space
        # 2^10 = 2^ 5 * 2^5
        # 2^5 = 2^2 * 2^2 * 2
        # 2^2 = 2^1 * 2^1
        # 2^1 = 2 * 2^0

        # recursive func
        # at each call, we will divide the exponential by 2
        # for even exponential, multiply the res by itself
        # for odd exponential, multiply the res by itself and by x

        # call the recursive in main
        # return res if n > 0 else return 1 / res

        res = self.rev(x, abs(n))
        return res if n >= 0 else (1/res)
        



        