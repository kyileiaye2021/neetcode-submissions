class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost.append(0)

        # # [1,2,3,0]

        # for i in range(len(cost) - 3, -1, -1):
        #     cost[i] += min(cost[i + 1], cost[i + 2])

        # return min(cost[0], cost[1])

        # two vars
        # 

        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[0]

        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])

        return min(cost[-1], cost[-2])