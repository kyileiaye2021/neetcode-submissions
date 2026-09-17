class Solution:
    def helper_recursion(self, n, memo):

        # base case
        if n == 1:
            return 1
        if n == 2:
            return 2

        if memo[n] != -1:
            return memo[n]

        memo[n] = self.helper_recursion(n - 1, memo) + self.helper_recursion(n - 2, memo)
        return memo[n]

    def climbStairs(self, n: int) -> int:
        # memoization
        memo = [-1] * (n + 1)
        return self.helper_recursion(n, memo)
        
