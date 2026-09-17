class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Input: prices = [10,1,5,6,7,1]
        # output: 6

        # Input: prices = [10,8,7,5,2]
        # Output: 0

        # two pointers
        max_profit = 0
        curr_profit = 0

        i, j = 0, 1

        while j < len(prices):

            if prices[j] > prices[i]:
                curr_profit = prices[j] - prices[i]

            else:
                i = j

            j += 1

            max_profit = max(max_profit, curr_profit)

        return max_profit





