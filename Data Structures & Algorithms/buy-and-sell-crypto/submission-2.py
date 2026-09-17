class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # if the next ele is less than the curr one, we can ignore any transaction  as we can make more profit

        # two pointer sliding window
        # start i  , j = 0 and 1

        # iterate thru the list until j reaches the end
        #   compare i and j ele
        #   if i ele is less than the j ele
        #       find the diff and get the max profit
        #       move j by 1
        #   else
        #       move i to j 
        #       move j by 1
        # return max profit

        i, j = 0, 1
        max_profit = 0
        while j < len(prices):
            if prices[i] < prices[j]:
                diff = prices[j] - prices[i]
                max_profit = max(max_profit, diff)

            else:
                i = j
            
            j += 1

        return max_profit