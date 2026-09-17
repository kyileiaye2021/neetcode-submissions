class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp
        # if we can reach to the end of string
        #   we can return True
        # iterate thru the str from the end
        #   try to find the match word in the wordDict for each substr [i:]
        #       if match: store true
        #   if the curr substr matched with one word, break the inner loop and go to the next char

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s)) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                
                # if the str is matched and separatable
                if dp[i]:
                    break

        return dp[0]