class Solution:
    def longestPalindrome(self, s: str) -> str:
        # happy cases
        # ababd -> bab, aba

        # abbc -> bb

        # edge cases
        # abcd -> a

        # a -> a

        # longest = 0
        # res_window = ''
        # iterate thru the str
        #   l = r = curr char
        #   while l > 0 and r < len (s) and l ele == r ele
        #       if curr window len > longest
        #           update longest 
        #           res window = curr window
        #       keep expanding
        #   
        #   l = curr char, r = i + 1
        #   while l > 0 and r < len (s) and l ele == r ele
        #       if curr window len > longest
        #           update longest 
        #           res window = curr window
        #       keep expanding
        # return res window

        longest = 0
        res_window = ''

        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_window_len = r - l + 1
                if longest < curr_window_len:
                    longest = curr_window_len
                    res_window = s[l:r + 1]

                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_window_len = r - l + 1
                if longest < curr_window_len:
                    longest = curr_window_len
                    res_window = s[l:r + 1]

                l -= 1
                r += 1

        return res_window

