class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if the total amount of cost > that of gas => return -1

        # iterate thru the eles in gas
        #   total curr gas += gas[i]
        #   total curr gas -= cost[i]
        #   if total curr gas < 0:
        #       total curr gas = 0
        #       start = i + 1
        #   else:
        #       start = i
        #   move to next i

        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                start = i + 1

        return start
