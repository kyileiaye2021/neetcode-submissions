class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Input: prices = [7,1,5,3,6,4]
        # output: 7

        # Input: prices = [1,2,3,4,5]
        # output: 4

        # two pointer
        # i, j 
        # total profit

        # until j is > len of prices
        # if j ele is greater than the prev ele
        #   find profit
        #   move j 
        #.  update the max profit

        # if j is less than the prev ele or j becomes len of prices
        #   move i to j 
        #   move j
        #   update the total profit
        #   reset max profit to 0

        i, j = 0, 1
        total_profit = 0
        curr_profit = 0

        while j < len(prices):
            print('current j ele: ', prices[j])
            if prices[j] > prices[j - 1]:
                curr_profit = prices[j] - prices[j - 1]

            else:
                i = j
                curr_profit = 0

            print(curr_profit)
            j += 1
            total_profit += curr_profit
    
        return total_profit




