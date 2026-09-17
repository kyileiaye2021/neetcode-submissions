class Solution:
    def climbStairs(self, n: int) -> int:
        # we can do recursion but it takes O(2^n)
        # if we do dp, it will take O(n) time

        # n =1
        # 1

        # n = 0
        # 0

        # dp 

        # arr
        # index --> step num in the path
        # val in the arr --> how many ways we can reach from the step to the n

        last = 1
        second_to_last = 1

        for i in range(n -1):
            temp = second_to_last
            second_to_last = last + second_to_last
            last = temp

        return second_to_last

