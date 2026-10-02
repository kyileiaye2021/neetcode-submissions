class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if total amount of gas < cost
        #   return -1

        # rem = 0
        # start = 0
        # iterate thru the ele
        #   if rem + gas[i] - cost[i] < 0:
        #      start = i + 1
        #      rem = 0
        #   else
        #       rem = rem + gas[i] - cost[i]
        # return start

        if sum(gas) < sum(cost):
            return -1


        rem = 0
        start = 0
        for i in range(len(gas)):
            if rem + gas[i] - cost[i] < 0:
                start = i + 1
                rem = 0
            
            else:
                rem = rem + gas[i] - cost[i]

        return start