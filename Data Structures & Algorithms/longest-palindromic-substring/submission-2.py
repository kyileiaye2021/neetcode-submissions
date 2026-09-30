class Solution:
    def longestPalindrome(self, s: str) -> str:
        # max substring
        # iterate thru the s
        #   if curr s ele == curr s + 1 ele
        #       keep track of curr substr and. keep expanding
        #   if curr s - 1 ele == curr s + 1 ele
        #       keep track of curr substr and keep expanding
        #   update max substring
        # return max_substring

        if len(s) == 1:
            return s

        res = ''
        max_window = 0

        for i in range(len(s)):
            
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_window = r - l + 1
                if max_window < curr_window:
                    res = s[l : r + 1]
                    max_window = curr_window

                l -= 1
                r += 1

            
            l = i 
            r = i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_window = r - l + 1
                if max_window < curr_window:
                    res = s[l : r + 1]
                    max_window = curr_window

                l -= 1
                r += 1

        return res











        

