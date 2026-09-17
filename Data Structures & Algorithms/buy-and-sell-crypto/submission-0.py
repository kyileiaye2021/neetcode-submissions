class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # happy cases
        # input: prices = [10,4,12,8]
        # output: 8

        # input: prices = [2,5,6]
        # output: 4

        # edge cases
        # input: prices = [5,4,3,2]
        # output: 0

        # input: prices = [2]
        # output: 0

        # Brute Force (O(n^2))
        # Two Pointers 

        # l,h
        # h will go thru the ele
        #   if h finds the smaller val than l pointer
        #       move the l 
        #       update h
        #   else:
        #       find profit
        #       update h
        # return max_profit

        l, h = 0, 1
        max_profit = 0
        while h < len(prices):
            if prices[h] < prices[l]:
                l = h
            
            else:
                profit = prices[h] - prices[l]
                max_profit = max(profit, max_profit)
            h += 1
        
        return max_profit


