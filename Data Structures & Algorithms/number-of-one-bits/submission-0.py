class Solution:
    def hammingWeight(self, n: int) -> int:
        # shift the bits to the left until 1 is met

        # n = 
        # count = 0
        # for c in n:
        #     if c == '1':
        #         count += 1

        # return count
        res = 0

        while n != 0:
            res += n % 2 
            n = n >> 1

        return res
