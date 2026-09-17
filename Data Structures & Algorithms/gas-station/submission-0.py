class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # sum up both arrays and check if the gas array cover the cost amount
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff

            if total < 0:
                # that starting point cannot cover the whole journey
                total = 0
                start = i + 1
        
        return start