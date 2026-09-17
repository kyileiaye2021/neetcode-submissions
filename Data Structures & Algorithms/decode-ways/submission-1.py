class Solution:
    def numDecodings(self, s: str) -> int:
        
        # happy cases
        # s = '12'
        # output 2

        # s = '126'
        # output: 3
        # 1, 2, 6
        # 1, 26
        # 12, 6

        # s = '10'
        # output: 1

        # s = '106'
        # 10, 6
        # output: 1

        # s = '0'
        # output: 0

        # s = '0002'
        # output: 0

        # s = '10001'
        # output: 0

        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            # one digit check
            if s[i] == '0':
                dp[i] = 0

            else:
                dp[i] = dp[i + 1]

            # two digit check
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                dp[i] += dp[i + 2]

        return dp[0]


