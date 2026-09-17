class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # happy cases
        # coins = [1,5,10]
        # amount = 12
        # 10 + 1 + 1 = 12

        # coins = [1,5,2]
        # amount = 26
        # 5 + 5 + 5 + 5 + 5 + 1

        # edge cases

        # coins = [2]
        # amount = 2
        # 1

        # coins = [3]
        # amount = 6
        # 2

        # coins = [3]
        # amount = 2
        # 0

        # coins = [10]
        # amount = 0
        # 0

        # dp arr which will store the num of coins to pay (index is the amount)
        # first amount 0 is goonna be 0 b/c to pay amount 0 the only way is paying no coins
        
        # [1,3,4,5], amount = 7
        # for paying amount 1, the num of coins is 1 
        # for paying amount 2, the num of coins is 2 coins of 1
        # for paying amount 3, the num of coin is 1 (we have coin 3)
        # dp[1] = 1
        # dp[2] = 2
        # dp[3] = 1

        # for each amount
        # we have to store the min of coins we can pay for each amount
        # try to add the coin and how many amount is left
        # for the amount left, retrieve how many coins we can use

        # for each amount
        #   for each coin
        #       amount left = curr amount - curr coin
        #       check if the amount left is >= 0
            #       retrieve the num of coins for the amount left
            #       store that 1 + num of coins retrieved to the curr dp[amoount]
            #       update the min coin num
        # return the min coin if the last dp slot is not default val else return -1

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                amount_left = i - c
                if amount_left >= 0:
                    curr_coin = 1 + dp[amount_left]
                    dp[i] = min(dp[i], curr_coin)

        return dp[-1] if dp[-1] != amount + 1 else -1
