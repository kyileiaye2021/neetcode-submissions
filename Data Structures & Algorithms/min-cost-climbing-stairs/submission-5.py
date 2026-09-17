class Solution:
    # def minCostHelper(self,cost, n, memo):
    #     # base case
    #     if n == 1 or n == 2:
    #         return memo[n]

    #     if memo[n] != -1:
    #         return memo[n]

    #     memo[n] = cost[n - 1] +  min(self.minCostHelper(cost, n -1, memo), self.minCostHelper(cost, n - 2, memo))
    #     return memo[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # memoizations
    
        # n = len(cost) + 1

        # using recursive func to break down n
        # memo arr to store the min costs in each step
        # we can reach nth stair from n-1 or n-2 step
        # get the minimum cost from the stairs
        # store the min cost in the nth position 
        # n = len(cost)

        # if n == 0:
        #     return 0

        # if n == 1:
        #     return cost[-1]

        # cost.append(0)
        # memo = [-1] * (n + 2)
        # memo[1] = cost[0]
        # memo[2] = cost[1]
        # return self.minCostHelper(cost, n + 1, memo)
        
        n = len(cost)
        dp = [0] * (n + 1)
        cost.append(0)

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(dp)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return dp[-1]

