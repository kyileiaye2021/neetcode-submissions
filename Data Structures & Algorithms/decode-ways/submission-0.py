class Solution:
    def numDecodings(self, s: str) -> int:
        
        # tabulation 
        # create a list with the size of len of s + 1
        # base case: assign the nth index to 1
        # iterate thru the str from the end to the first ele
        #   if the curr ele is not '0' ( single digit )
        #       update the curr ele with the curr index + 1 ele 
        #   if the curr index + 1 is within the range of s len and curr index is 1 or curr index is 2 
        #   and the next index is within the range of 0-6  (double digit)
        #       update the curr ele with the curr index + 2 ele

        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1 # base case

        for i in range(n - 1, -1, -1):
            if s[i] != '0':
                dp[i] = dp[i + 1] # single digit
            
                if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                    dp[i] += dp[i + 2] # double digit

        return dp[0]